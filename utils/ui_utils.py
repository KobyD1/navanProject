class uiUtils:
    def clear_and_type_element(self, element, text):
        element.click()
        element.clear()
        element.type(text)
