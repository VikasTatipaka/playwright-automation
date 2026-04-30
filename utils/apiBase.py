from playwright.sync_api import Playwright
orders_payload = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}
login_payload = {"userEmail":"vickyipad4@icloud.com","userPassword":"Vikas@123"}
# https://rahulshettyacademy.com/api/ecom/order/create-order

class APIutils:

    def get_token(self,playwright: Playwright):
        request_context = playwright.request.new_context(base_url= "https://rahulshettyacademy.com")
        login_response= request_context.post("/api/ecom/auth/login", data = login_payload, headers = {"Content-Type": "application/json",})
        assert login_response.ok
        response_json = login_response.json()
        return response_json["token"]

    def createOrder(self,playwright: Playwright):
        token= self.get_token(playwright)
        api_request_context=  playwright.request.new_context(base_url= "https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                data= orders_payload, headers={"Content-Type": "application/json",
                                                               "Authorization": token})
        response_json = response.json()
        order_id= response_json["orders"][0]
        return order_id