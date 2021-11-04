import pymongo

# 连接数据库
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
# 创建数据库
mongo_db = mongo_client['数据库名字']
# 在其中创建集合
mongo_collection = mongo_db['集合名字']

# 插入多条数据 insert_many()
info_1 = {
    'name': 'Zarten_1',
    'text': 'Inserting a Document',
    'tags': ['a', 'b', 'c'],

}

info_2 = {
    'name': 'Zarten_2',
    'text': 'Inserting a Document',
    'tags': [1, 2, 3],

}

insert_list = [info_1, info_2]
mongo_collection.insert_many(insert_list)
# 每个文档是字典，然后用insert_many(列表)插入

# 查询多条数据 find()
# 返回满足条件的所有结果，返回类型为 Cursor ，通过迭代获取每个查询结果，每个结果类型为dict字典

find_result_cursor = mongo_collection.find()
for find_result in find_result_cursor:
    print(find_result)
