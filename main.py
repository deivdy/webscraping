#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
require chrome version >= 61.0.3119.0
headless mode
"""


import time
import pychrome


class EventHandler(object):
    def __init__(self, browser, tab):
        self.browser = browser
        self.tab = tab
        self.start_frame = None
        self.is_first_request = True
        self.html_content = None

    def frame_started_loading(self, frameId):
        if not self.start_frame:
            self.start_frame = frameId

    def request_intercepted(self, interceptionId, request, **kwargs):
        if self.is_first_request:
            self.is_first_request = False
            headers = request.get('headers', {})
            headers['Test-key'] = 'test-value'
            self.tab.Network.continueInterceptedRequest(
                interceptionId=interceptionId,
                headers=headers,
                method='POST',
                postData="hello post data: %s" % time.time()
            )
        else:
            self.tab.Network.continueInterceptedRequest(
                interceptionId=interceptionId
            )

    def frame_stopped_loading(self, frameId):
        if self.start_frame == frameId:
            self.tab.Page.stopLoading()
            result = self.tab.Runtime.evaluate(expression="document.documentElement.outerHTML")
            self.html_content = result.get('result', {}).get('value', "")
            print(self.html_content)
            self.tab.stop()


def close_all_tabs(browser):
    if len(browser.list_tab()) == 0:
        return

    for tab in browser.list_tab():
        try:
            tab.stop()
        except pychrome.RuntimeException:
            pass

        browser.close_tab(tab)

    time.sleep(1)
    assert len(browser.list_tab()) == 0


def main():
    browser = pychrome.Browser()

    # close_all_tabs(browser)

    tab = browser.new_tab()

    eh = EventHandler(browser, tab)
    tab.Network.requestIntercepted = eh.request_intercepted
    tab.Page.frameStartedLoading = eh.frame_started_loading
    tab.Page.frameStoppedLoading = eh.frame_stopped_loading

    tab.start()
    # Habilitar o Runtime
    tab.Runtime.enable()
    # call method
    tab.Network.enable()

    tab.Page.stopLoading()
    tab.Page.enable()
    # tab.Network.setRequestInterceptionEnabled(enabled=True)
    tab.Page.navigate(url="https://jsonplaceholder.typicode.com/posts/1")
        

    tab.wait(60)
    tab.stop()
    browser.close_tab(tab)
        

    print('Done')


if __name__ == '__main__':
    main()