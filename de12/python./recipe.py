import requests
import re
from bs4 import BeautifulSoup
import json
 
# User-Agent
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/Chrome/84.0.4147.135 Safari/537.36"
 
def get_html(url, params=None, headers=None):
 
    try:
        # データ取得
        resp = requests.get(url, params=params, headers=headers)
        resp.encoding = 'utf8'  # 文字コード
         
        # 要素の抽出
        soup = BeautifulSoup(resp.text, "html.parser")
        return soup
    except Exception as e:
        return None
 
def get_page_info(url):
     
    # 結果
    result = {}
         
    # データ取得
    params = {}
    headers = {"User-Agent": user_agent}
    soup = get_html(url, params, headers)
 
    if soup != None:
         
        try:
            json_str_elem = soup.find(id="hydration_initial_state")
            json_str = get_text_by_elem(json_str_elem)
            json_load = json.loads(json_str)
            data_dic = json_load["state"]["fetchVideo"]["data"]["data"]
            ingredients_inline = data_dic["attributes"]
             
            if data_dic:
                recipe_id = data_dic["id"]
                recipe_name = data_dic["attributes"]["title"]
                detail = data_dic["attributes"]["detail-content"]
                video_url = data_dic["attributes"]["mp4-url"]
                img_small_url = data_dic["attributes"]["thumbnail-square-small-url"]
                img_normal_url = data_dic["attributes"]["thumbnail-square-normal-url"]
                img_large_url = data_dic["attributes"]["thumbnail-square-large-url"]
                cooking_time = data_dic["attributes"]["cooking-time"]
                published_datetime = data_dic["attributes"]["published-at"]
                introduction = data_dic["attributes"]["introduction"]
                ingredients = data_dic["attributes"]["ingredients"]
                ingredients_inline = data_dic["attributes"]["ingredients-inline"]
                expense = data_dic["attributes"]["expense"]
                memo = data_dic["attributes"]["memo"]
                servings_str = data_dic["attributes"]["servings"]
                 
                servings_val = 0
                if servings_str:
                    servings_dic = re.findall(r'\d+', servings_str)
                    servings_val = servings_dic[0]
                 
                result["recipe_id"] = recipe_id
                result["recipe_name"] = recipe_name
                result["detail"] = detail
                result["video_url"] = video_url
                result["img_small_url"] = img_small_url
                result["img_normal_url"] = img_normal_url
                result["img_large_url"] = img_large_url
                result["cooking_time"] = cooking_time
                result["published_datetime"] = published_datetime
                result["introduction"] = introduction
                result["ingredients_inline"] = ingredients_inline
                result["introduction"] = introduction
                result["expense"] = expense
                result["memo"] = memo
                result["servings_str"] = servings_str
                result["servings_val"] = servings_val
                     
                ingredient_list = []
                 
                for ingredient in ingredients:
                     
                    ingredient_dic = {}
                     
                    ingredient_id = ingredient["id"]
                    ingredient_type = ingredient["type"]
                     
                    if ingredient_type=="ingredients":
                        ingredient_group_id = ingredient["group-id"]
                        ingredient_title = ingredient["name"]
                        ingredient_name = ingredient["actual-name"]
                        ingredient_amount = ingredient["quantity-amount"]
                         
                    else:
                        ingredient_title = ingredient["title"]
                        ingredient_group_id = 0
                        ingredient_name = ""
                        ingredient_amount = ""
                     
                    ingredient_dic["ingredient_id"] = ingredient_id
                    ingredient_dic["ingredient_type"] = ingredient_type
                    ingredient_dic["ingredient_title"] = ingredient_title
                    ingredient_dic["ingredient_name"] = ingredient_name
                    ingredient_dic["ingredient_amount"] = ingredient_amount
                     
                    ingredient_list.append(ingredient_dic)
                     
                result["ingredient_list"] = ingredient_list
                     
        except Exception as e:
            return None
    else:
        print("エラー")
     
    return result
 
def get_text_by_elem(elem):
     
    try:
        text = elem.text
        text = text.strip()  
        return text
    except Exception as e:
        return None
     
if __name__ == '__main__':
     
    url = "https://www.kurashiru.com/recipes/ec28c79c-07ff-4e3e-b011-be628982eec3"
     
    result = get_page_info(url)
    print(result)