from selenium.webdriver import Keys
from seleniumbase import SB
from seleniumbase import BaseCase
class CreateTeamTest(BaseCase):
    def test_create_team(sb):
        with SB(uc=True) as sb:
            # ----------------------------------------------------------------------------------------------------------
            # LOGIN, CREATE COMPANY , CREATE TEAM, Navigate To Overview Page, NAVIGATE TO BOARD PAGE, Create Board List
            # Create Card, Add Notes, Set Due Date.
            # ----------------------------------------------------------------------------------------------------------
            # Login
            sb.open("https://staging.cicle.app/signin")
            sb.click('//*[@id="root"]/div/div[2]/div[2]/div[1]')
            sb.type('input[type="email"]', "lordula196")
            sb.click('//*[@id="identifierNext"]/div/button/div[1]')
            sb.type('input[type="password"]', "qwerty17;")
            sb.click('//*[@id="passwordNext"]/div/button/div[1]')
            sb.assert_text("Hello and welcome to Cicle!", "h1")
            sb.save_screenshot("Login Success", "Custom_Screenshots")
            sb._print("Login Success")
            # ----------------------------------------------------------------------------------------------------------
            # Create Company
            sb.click('img[src="data:image/png;base64,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"]')
            sb.type('input[name="name"]', "Company1")
            sb.type('textarea[name="desc"]', "Company1")
            sb.click('h1:contains("Create Company")')
            sb.save_screenshot("Create Company", "Custom_Screenshots")
            sb._print("Create Company Success")
            # ----------------------------------------------------------------------------------------------------------
            # Create Team
            sb.click("div#root div:nth-of-type(3) div:nth-of-type(4)")
            sb.click("div#root div:nth-of-type(3) div:nth-of-type(3) div:nth-of-type(2) div:nth-of-type(2) img")
            sb.type('input[name="name"]', "Team1")
            sb.type('textarea[name="desc"]', "Team1")
            sb.click('//*[@id="root"]/div[3]/div[3]/div[2]/div[2]/div[2]/button/div/h1')
            sb.save_screenshot("Create Team", "Custom_Screenshots")
            sb._print("Create Team Success")
            # ----------------------------------------------------------------------------------------------------------
            # Navigate To Overview Page
            sb.click('//*[@id="root"]/div[3]/div[4]/a/div/div[1]/p')
            # ----------------------------------------------------------------------------------------------------------
            # Navigate To Board
            sb.click('img[src="/static/media/board.82e692f2.png"]')
            sb.click("div.ListContainer_ListContainer__outerList__1PG0- > div > button > div > div")
            sb.save_screenshot("Navigate To Board", "Custom_Screenshots")
            sb._print("Success Navigate To Board")
            # ----------------------------------------------------------------------------------------------------------
            # Create BoardList
            sb.type('input[name="name"]', "Board1")
            sb.click("div.ListContainer_ListContainer__outerList__1PG0- div form div:nth-of-type(2) button div")
            sb.save_screenshot("Create BoardList", "Custom_Screenshots")
            sb._print("Success Create BoardList")
            # ----------------------------------------------------------------------------------------------------------
            # Create Card
            sb.click("div.ListContainer_ListContainer__outerList__1PG0- div div:nth-of-type(4) a")
            sb.type("input.form-control", "Card")
            sb.click("div.ListContainer_ListContainer__outerList__1PG0- div div:nth-of-type(4) div:nth-of-type(3) button div")
            sb.refresh()
            sb.save_screenshot("Create Card", "Custom_Screenshots")
            sb._print("Success Create Card")
            # ----------------------------------------------------------------------------------------------------------
            # Navigate To Card Page
            sb.hover_and_click('//*[@id="listcard_content-0"]/div[1]/div/div/a', '//*[@id="listcard_content-0"]/div[1]/div/div/a')
            sb.save_screenshot("Navigate To Card Page", "Custom_Screenshots")
            sb._print("Success Navigate To Card Page")
            # ----------------------------------------------------------------------------------------------------------
            # Add Comment
            sb.click('//*[@placeholder="Add new comment..."]')
            sb.type('//*[@id="cardModal"]/div/div/div[1]/div[7]/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/p', "Add Comment")
            sb.click('//*[@class="Main_iconText__f-xVC Main_iconDefault__3fDo9 Main_iconPositionStart__IWQqT"]')
            sb.save_screenshot("Add Comment", "Custom_Screenshots")
            sb._print("Success Add Comment")
