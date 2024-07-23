import json

def process_history(history_data):
   # 获取历史记录的键（即日期）
    dates = sorted(history_data.keys())

    while len(dates) > 12:
        oldest_date = dates.pop(0)
        del history_data[oldest_date]
        print(f"删除了历史记录：{oldest_date}")
        
        
    
    return history_data

# 加载 Json 文件
with open('history.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for ts, ts_data in data["吉隆坡机场APM300R项目CIB执行管理台账history"].items():

        # 处理历史记录
        data["吉隆坡机场APM300R项目CIB执行管理台账history"][ts] = process_history(data["吉隆坡机场APM300R项目CIB执行管理台账history"][ts])

# 保存更新后的 Json 数据
with open('history.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)