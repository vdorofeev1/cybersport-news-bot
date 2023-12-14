from script.cybersport_requests.login_request import login_request
from script.cybersport_requests.materials_request import materials_request
from script.cybersport_requests.slug_request import slug_request, clean_text


def get_news():
    response = []
    login_response = login_request()
    login_token, login_refresh_token, status_code = login_response["token"], login_response["refresh_token"], int(
        login_response["status_code"])

    if status_code == 200:
        materials_response = materials_request(login_token, login_refresh_token)
        materials = materials_response["data"]

        for material in materials:
            slug = material["attributes"]["slug"]
            title = material["attributes"]["title"]

            message = ""
            message += "\n" + title + "\n\n"

            slug_response = slug_request(slug, login_token, login_refresh_token)
            blocks = slug_response["data"]["attributes"]["content"]["blocks"]

            for block in blocks:
                data = block["data"]
                if "text" in data:
                    text = block["data"]["text"]

                    message += clean_text(text) + "\n"
            response.append(message)
    return response
