# AUTOGENERATED FILE! PLEASE DON'T EDIT
"""All tools related to the MGI database. Expected to use behind the "mgi"
module name, like this::

    from k1lib.bioinfo.cli import *
    ["SOD1", "AMPK"] | mgi.batch()
"""
import k1lib.bioinfo.cli as _cli
from k1lib.bioinfo.cli.init import BaseCli as _BaseCli
from typing import List as _List
import time as _time
class batch(_BaseCli):
    """Queries MGI database, convert list of genes to MGI ids"""
    def __init__(self, headless=True):
        """
:param headless: whether to run this operation headless, or actually
    display the browser"""
        super().__init__(); self.headless = headless
    def __ror__(self, it:_List[str]):
        super().__ror__(it)
        import selenium; from selenium import webdriver
        query = "\n".join(it | _cli.strip() | ~_cli.isValue(""))
        options = selenium.webdriver.chrome.options.Options()
        if self.headless: options.add_argument("--headless")
        driver = selenium.webdriver.Chrome(options=options);
        print("\r1/4 Going to website...  ", end="")
        driver.get("http://www.informatics.jax.org/batch")
        print("\r2/4 Submitting data...   ", end="")
        driver.find_element_by_name("ids").send_keys(query)
        driver.find_element_by_css_selector("tr.queryControls > td > input.buttonLabel").click()
        markerIds = []; terms = []; names = []; features = []
        print("\r3/4 Getting data...      ", end="")
        def getStuff(classEnd:str):
            return [elem.get_attribute("textContent") for elem in driver.find_elements_by_css_selector(f".yui-dt-col-{classEnd} > div")]
        while len(markerIds) <= 1:
            markerIds = getStuff("markerId"); terms = getStuff("term")
            names = getStuff("name"); features = getStuff("feature")
            _time.sleep(1)
        print("\r4/4 Data received!       ")
        driver.close()
        return _cli.joinColumns([markerIds, terms, features, names])