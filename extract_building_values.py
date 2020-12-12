import argparse
import pandas as pd


def get_args():
    parser = argparse.ArgumentParser(description='Extract')
    parser.add_argument('building_file', type=str, help='Path of building_values.txt')
    return parser.parse_args()


def building_values_to_dicts(building_file):
    dicts = dict()
    current_dict_name = None
    current_values = dict()
    with open(building_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if 'Nothing below this line should need to be edited if you want to change building balance' in line:
            break
        if line[0] == '#' and line[1] != '#' and len(line.split('#')) == 3:
            if len(current_values) > 0:
                dicts[current_dict_name] = current_values
            current_dict_name = line.split('#')[1][1:-1]
            current_values = dict()
        if line[0] == '@':
            if '_base' in line:
                current_values[line[1:line.index('_base')]] = {'base': float(line.split('=')[1])}
            elif 'scale_addition_per_tier' in line:
                current_values[line[1:line.index('_scale_addition_per_tier')]]['scale_addition_per_tier'] = float(line.split('=')[1])
    return dicts


def get_max_tier(value):
    if value == 'main_cost':
        return 5
    if value == 'tribal_cost':
        return 2
    return 8

def dicts_to_dfs(dicts):
    dfs = dict()
    for section in dicts:
        df = pd.DataFrame()
        for key in dicts[section]:
            if 'scale_addition_per_tier' in dicts[section][key]:
                for i in range(1, get_max_tier(key) + 1):
                    value = dicts[section][key]['base'] + (i - 1) * dicts[section][key]['scale_addition_per_tier']
                    df = pd.concat([df, pd.DataFrame(data=[(f'{key}_tier_{i}', value)],
                                                       columns=['Name', 'Value'])], axis=0, ignore_index=True)
                df = pd.concat([df, pd.DataFrame(data=[(None, None)],
                                           columns=['Name', 'Value'])], axis=0, ignore_index=True)
            else:
                value = dicts[section][key]['base']
                df = pd.concat([df, pd.DataFrame(data=[(key, value)],
                                                 columns=['Name', 'Value'])], axis=0, ignore_index=True)
        dfs[section] = df
    return dfs


if __name__ == '__main__':
    dicts = building_values_to_dicts(get_args().building_file)
    dfs = dicts_to_dfs(dicts)
    writer = pd.ExcelWriter('building_values.xlsx')
    for section in dfs:
        dfs[section].to_excel(writer, sheet_name=section)
    writer.save()
