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

BillType API
============
创建类型
----
- url: /bill_type/post
- method: POST
- params:
    * name String
- return:

        {
            "code": 0,
        }

获取类型列表
------
- url: /bill_type/list
- method: GET
- params:
    * 
- return:

		{
		    "code": 0,
		    "result":
		    [
		        {
		            "id": 1,
		            "name": "name"
		        }
		        ...
		    ]
		}

获取类型
----
- url: /bill_type/detail/:id
- method: GET
- params:
	* id Int
- return:

		{
		    "code": 0,
		    "result":
	        {
	            "id": 1,
	            "name": "",
	        },
		}

更新类型
----
- url: /bill_type/update
- method: PUT
- params:
    * id Int
    * name String
- return:

        {
            "code": 0,
        }

删除一条账单
---
- url: /bill_type/delete/:id
- method: DELETE
- params:
	* id Int
- return:

		{
		    "code": 0,
		}

