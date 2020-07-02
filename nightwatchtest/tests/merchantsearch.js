module.exports = {
    '@tags': ['merchant'],
    'Merchant Search : Walmart'(browser){
        const mainQuery = 'Walmart'
        const mainQueryInputSelector = 'input[id = "searchWrapper"]';
        browser
            .url("http://localhost:8000/customer/view_merchants/")
            .setValue(mainQueryInputSelector, mainQuery)
            .saveScreenshot('tests_output/merchant-search.png')
    } 
}