from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_btn()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_curt_msg()
    page.should_be_equal_name_product_and_added_product()
    page.should_be_cart_value()
    page.should_be_equal_price_product_and_added_product()
