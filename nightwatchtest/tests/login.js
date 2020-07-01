module.exports = {
    '@tags': ['login'],
    'Consumer Login'(browser){
        const username = 'ankur';
        const password = 'qwertyuiop@1234';
        const loginButton = '.a[class = "btn-solid-lg page-scroll"]';
        const userNameSelector = 'input[name = "username"]';
        const passSelector = 'input[name = "password"]';
        const submitSelector = 'input[type = "submit"]';

        browser
            .url("http://localhost:8000/")
            .click(loginButton)
            .setValue(userNameSelector, username)
            .setValue(passSelector, password)
            .click(submitSelector)
            .saveScreenshot('tests_output/merchant-search.png')
    } 
}