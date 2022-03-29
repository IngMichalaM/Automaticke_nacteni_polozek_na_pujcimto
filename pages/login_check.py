
def login_check(page, log):
    """ Check the login
        If the login was not successful, ask the user to either try to log in again,
        or to end the process.
    """

    while True:
        # check the login
        res = page.check_logged_in()

        if res:
            log.info('Log in was successful')
            break
            # else go on again with the login

        if 'Login nebo heslo není správné' in page.driver.page_source:
            log.info('Login was not successful.')
            go_on_with_login = input('Do you want to log manually? (y/n): ')

            if go_on_with_login.lower() == 'y':
                page.goto_login_page()
                login_email, login_password = page.input_credentials()
                page.send_credentials(login_email, login_password)
                log.info('Trying to login again.')
            else:
                print('You did not want to log in after unsuccessful login. Bye.')
                log.info('You have left.')
                page.driver.close()
                quit()
        else:
            print('Unknown problem.')
            log.info('Unknown problem. Leaving.')
            page.driver.close()
            quit()
