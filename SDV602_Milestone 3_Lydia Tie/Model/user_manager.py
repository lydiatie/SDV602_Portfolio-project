import sys
sys.path.append(".")
from Model.jsn_drop_service import jsnDrop  
from time import gmtime


class UserManager(object):
    current_user = None
    current_pass = None
    current_status = None
    current_screen = None
    stop_thread = False
    chat_list = None
    this_user_manager = None

    def now_time_stamp(self):
        time_now = gmtime()
        timestamp_str = f"{time_now.tm_year}-{time_now.tm_mon}-{time_now.tm_mday} {time_now.tm_hour}:{time_now.tm_min}:{time_now.tm_sec}"
        return timestamp_str
 

    def __init__(self) -> None:
        super().__init__()

        self.jsnDrop = jsnDrop("dd6fb593-50ea-4463-bf56-e92e240a45cc","https://newsimland.com/~todd/JSON")

        # SCHEMA Make sure the tables are  CREATED - jsnDrop does not wipe an existing table if it is recreated
        result = self.jsnDrop.create("tblUser",{"PersonID PK":"A_LOOONG_NAME"+('X'*50),
                                                "Password":"A_LOOONG_PASSWORD"+('X'*50),
                                                "Status":"STATUS_STRING",
                                                "DesNo": 10})

        result = self.jsnDrop.create("tblChat",{"Time PK": self.now_time_stamp()+('X'*50),
                                                "PersonID":"A_LOOONG_NAME"+('X'*50),
                                                "DesNo":10,
                                                "Chat":"A_LOONG____CHAT_ENTRY"+('X'*255)})
        UserManager.this_user_manager = self

    def register(self, user_id, password):
        api_result = self.jsnDrop.select("tblUser",f"PersonID = '{user_id}'") # Danger SQL injection attack via user_id?? Is JsnDrop SQL injection attack safe??
        if( "DATA_ERROR" in self.jsnDrop.jsnStatus): # we get a DATA ERROR on an empty list - this is a design error in jsnDrop
            # Is this where our password should be SHA'ed !?
            result = self.jsnDrop.store("tblUser",[{'PersonID':user_id,'Password':password,'Status':'Registered', "DesNo": 0}])
            UserManager.currentUser = user_id
            UserManager.current_status = 'Logged Out'
            result = "Registration Success"
        else:
            result = "User Already Exists"

        return result

    def login(self, user_id, password):
        result = None
        api_result = self.jsnDrop.select("tblUser",f"PersonID = '{user_id}' AND Password = '{password}'") # Danger SQL injection attack via user_id?? Is JsnDrop SQL injection attack safe??
        api_result1 = self.jsnDrop.select("tblUser",f"PersonID = '{user_id}' AND Status = 'Logged In'")
        
        if not("Data error" in api_result1): # check if user is logged in or not. if no data error means user is logged in
            result = "User has already logged in"
            UserManager.current_status = "Logged Out"
            UserManager.current_user = None
        
        elif("Data error" in api_result): # then the (user_id,password) pair do not exist - so bad login
            result = "Wrong username or password"
            UserManager.current_status = "Logged Out"
            UserManager.current_user = None

        else:
            UserManager.current_status = "Logged In"
            UserManager.current_user = user_id
            UserManager.current_pass = password
            api_result = self.jsnDrop.store("tblUser",[{"PersonID":user_id,"Password":password,"Status":"Logged In", "DesNo": 0}])
            result = "Login Success"

        return result

    def get_online_user(self):
        api_result = self.jsnDrop.select("tblUser", "Status = 'Logged In'")
        online_user = []

        for value in api_result:
            online_user.append(value['PersonID'])
        
        return online_user

    def get_des_user(self, DesNo):
        api_result = self.jsnDrop.select("tblUser", f"Status = 'Logged In' AND DesNo = {DesNo}")
        des_user = []

        for value in api_result:
            des_user.append(value['PersonID'])
        
        return des_user

    def set_current_DES(self, DesNo):
        result = None
        if UserManager.current_status == "Logged In":
            user_id = UserManager.current_user
            password = UserManager.current_pass
            api_result = self.jsnDrop.store("tblUser",[{"PersonID":user_id,"Password":password,"Status":"Logged In", "DesNo": DesNo}])
            UserManager.current_screen = DesNo
            result = "Set Screen"
        else:
            result = "Log in to set the current screen"
        return result

    def logout(self):
        result = "Must be 'Logged In' to 'LogOut' "
        if UserManager.current_status == "Logged In":
            api_result = self.jsnDrop.store("tblUser",[{"PersonID": UserManager.current_user,
                                                        "Password": UserManager.current_pass,
                                                        "Status":"Logged Out",
                                                        "DesNo": 0}])
            if not("ERROR" in api_result):
                UserManager.current_status = "Logged Out"
                result = "Logged Out"
            else:
                result = self.jsnDrop.jsnStatus

        return result

    def send_chat(self, message):
        result = None
        if UserManager.current_status != "Logged In":
            result = "Please log in to chat"
        elif UserManager.current_screen == None:
            result = "Chat not sent. Not in DES"
        else:
            user_id = UserManager.current_user
            des_screen = UserManager.current_screen
            api_result = self.jsnDrop.store("tblChat",[{"Time": self.now_time_stamp(),
                                                        "PersonID": user_id,
                                                        "DesNo": f'{des_screen}',
                                                        "Chat": message}])
            if "STORE tblChat executed" in api_result:
                result = "Chat sent"
            else:
                result = self.jsnDrop.jsnStatus

        return result
    
    def get_chat(self, DesNo):
        api_result = self.jsnDrop.select("tblChat", f"DesNo = {DesNo}")

        chat_lists = []
        messages = ""

        if not 'Data error' in api_result:

            sorted_chats = sorted(api_result, key=lambda i: i['Time'])

            if len(sorted_chats) >= 5:
                chat_lists = sorted_chats[-5:]
                for value in chat_lists:
                    msg_string = f"[{value['PersonID']}]:{value['Chat']} \t(sent at {value['Time']})\n"
                    messages += msg_string

            else:
                for value in sorted_chats:
                    msg_string = f"[{value['PersonID']}]:{value['Chat']} \t(sent at {value['Time']})\n"
                    messages += msg_string 
        else:
            messages = ""

        return messages


