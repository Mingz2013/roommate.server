API标准
===
正确返回
---

	{
	    "code": 0,  #结果码=0
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

User API
========
创建用户
----
- url: /user/post
- method: POST
- params:
    * name String
    * nick String
    * mobile String
    * email String
    * password String
- return:

        {
            "code": 0,
        }

获取用户列表
------
- url: /user/list
- method: GET
- params:
    * 
- return:

		{
		    "code": 0,
		    "result":
		    [
		        {
		            "nick": "xwdoor",
		            "mail": "xwdoor@126.com",
		            "password": "xwdoor",
		            "mobile": "18684033888",
		            "name": "肖威",
		            "id": 0
		        }
		        ...
		    ]
		}

获取用户详细信息
--------
- url: /user/detail/:id
- method: GET
- params:
	* id Int
- return:

		{
		    "code": 0,
		    "result":
	        {
		            "nick": "xwdoor",
		            "mail": "xwdoor@126.com",
		            "password": "xwdoor",
		            "mobile": "18684033888",
		            "name": "肖威",
		            "id": 0
		    },
		}

更新用户信息
------
- url: /user/update
- method: PUT
- params:
    * id Int
    * nick String
    * password String
    * name String
    * mobile String
    * email String
- return:

        {
            "code": 0,
        }

删除一个用户
------
- url: /user/delete/:id
- method: DELETE
- params:
	* id Int
- return:

		{
		    "code": 0,
		}

