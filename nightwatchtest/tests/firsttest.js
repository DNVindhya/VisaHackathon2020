module.exports = {
    'My first test case'(browser) {
        browser
            .url("http://localhost:8000/")
            .waitForElementVisible('.text-container')
            .assert.containsText(".text-container", "Covid Support by Visa");
    }
}