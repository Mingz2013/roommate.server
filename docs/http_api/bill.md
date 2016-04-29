API标准
===
正确返回
---

	{
	    "code": 0,  # 结果码=0
	    "result": {}
	}

错误返回
---

	{
	    "code": 1001,  # 不等于0的数字代表错误
	    "error": "错误信息"
	}
	错误码编号：
	* 1001
	* 1002
	* other

Bill API
===
提交账单
---
- url: /bill/post
- method: POST
- params:
    * record_user_id Int # 记录者
    * spend_user_id Int # 消费者
    * type_id Int
    * desc String
    * money Float
    * date Date
- return:

        {
            "code": 0,
        }

获取账单列表
---
- url: /bill/list
- method: GET
- params:
    * 
- return:

		{
		    "code": 0,
		    "result":
		    [
		        {
		            "desc": "描述",
		            "date": "2016-03-21 08:50:43",
		            "type_name": "",
		            "id": 1,
		            "money": 35.5,
		            "record_user_name": "",
		            "spend_user_name": "",
		        }
		        ...
		    ]
		}

根据user_id获取消费的账单列表
------------------
- url: /bill/list/int:user_id
- method: GET
- params:
    * user_id Int
- return:

		{
		    "code": 0,
		    "result":
		    [
		        {
		            "desc": "描述",
		            "date": "2016-03-21 08:50:43",
		            "type_name": "",
		            "id": 1,
		            "money": 35.5,
		            "record_user_name": "",
		            "spend_user_name": "",
		        }
		        ...
		    ]
		}

获取账单详情
---
- url: /bill/detail/int:id
- method: GET
- params:
	* id Int
- return:

		{
		    "code": 0,
		    "result":
	        {
	            "desc": "描述",
	            "date": "2016-03-21 08:50:43",
	            "type_name": "",
	            "id": 1,
	            "money": 35.5,
	            "record_user_name": "",
	            "spend_user_name": "",
	        },
		}

更新一条账单
---
- url: /bill/update
- method: PUT
- params:
    * id Int
    * record_user_id Int # 记录者
    * spend_user_id Int # 消费者
    * type_id Int
    * desc String
    * money Float
    * date Date
- return:

        {
            "code": 0,
        }

删除一条账单
---
- url: /bill/delete/int:id
- method: DELETE
- params:
	* id Int
- return:

		{
		    "code": 0,
		}

