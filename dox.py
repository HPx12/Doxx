import requests

import sys

from bs4 import BeautifulSoup

import json

from colorama import Fore



if "-h" in sys.argv:

  print(Fore.GREEN + ''' 

                               /T /I

                              / |/ | .-~/

                          T\ Y  I  |/  /  _

         /T               | \I  |  I  Y.-~/

        I l   /I       T\ |  |  l  |  T  /

     T\ |  \ Y l  /T   | \I  l   \ `  l Y

 __  | \l   \l  \I l __l  l   \   `  _. |

 \ ~-l  `\   `\  \  \  ~\  \   `. .-~   |

  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |

.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./

 >--.  ~-.   ._  ~>-"    " \   7   7   ]

^.___~"--._    ~-{  .-~ .  `\ Y . /    |

 <__ ~"-.  ~       /_/   \   \I  Y   : |

   ^-.__           ~(_/   \   >._:   | l______

       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.

              (_/ .  ~(   /'     "~"--,Y   -=b-. _)

               (_/ .  \  :           / l      c"~o \ 

                \ /    `.    .     .^   \_.-~"~--.  )

                 (_/ .   `  /     /       !       )/

                  / / _.   '.   .':      /        '

                  ~(_/ .   /    _  `  .-<_

                    /_/ . ' .-~" `.  / \  \          ,z=.

                    ~( /   '  :   | K   "-.~-.______//

                      "-,.    l   I/ \_    __{--->._(==.

                       //(     \  <    ~"~"     //

                      /' /\     \  \     ,v=.  ((

                    .^. / /\     "  }__ //===-  `

                   / / ' '  "-.,__ {---(==-

                 .^ '       :  T  ~"   ll       

                / .  .  . : | :!        \ 

               (_/  /   | | j-"          ~^

                 ~-<_(_.^-~"

''')

  print(Fore.GREEN + 'USAGE: \n [-h] FOR PRINTING THIS OUT\n [-ip] FOR EXAMPLE "python dox.py -ip [victim ip]"\n [-o] FOR SAVING THE RESULT IN A TEXT FILE FOR EXAMPLE "python dox.py -ip [victim ip] -o"\n [-S] FOR SUMMARY FOR EXAMPLE "python dox.py -ip [victim ip] -S"\n [-V] FOR VPN FOR EXAMPLE "python dox.py -ip [victim ip] -V"\n [-H] FOR HOSTING FOR EXAMPLE "python dox.py -ip [victim ip] -H"\n [-M] FOR MALICIOUS-INFO\n [-P] FOR PRIVACY THREAT FOR EXAMPLE "python dox.py -ip [victim ip] -P"\n [-Safe] FOR SAFE DNS SERVER FOR EXAMPLE "python dox.py -ip [victim ip] -Safe"\n [-CAM] SEARCH CAMERAS IN VICTIM AREA FOR EXAMPLE "python dox.py -CAM -Country [VICTIM COUNTRY] -City [VICTIM CITY]"\n [-GOOGLEMAPS] THIS WILL SEARCH FOR THE VICTIM LIVING PLACE WITH LONGITUDE AND LATITUDE FOR EXAMPLES "python dox.py -GOOGLEMAPS -LONG [VICTIM LONG] -LAT [VICTIM LAT]" #NOTE: IF YOU TAKE THE LONG AND THE LAT FROM THIS TOOL MAKE SURE YOU FILP THEM AND THE LONG WILL BE LAT AND THE LAT WILL BE LONG OTHERWISE IT WILL NOT GIVE YOU THE RIGHT LOCATION')

  quit()





if "-CAM" in sys.argv:

  if "-Country" in sys.argv:

    country = sys.argv[3]

  

  if "-City" in sys.argv:

    city = sys.argv[5]

  

  url = f"https://www.criminalip.io/en/asset/search?query=webcam+country%3A+{country}+city%3A+{city}"

  print("CAMS ---->",url)

  quit()



if "-GOOGLEMAPS" in sys.argv:

  if "-LONG" in sys.argv:

    LONG = sys.argv[3]

  

  if "-LAT" in sys.argv:

    LAT = sys.argv[5]

  

  url = f"https://www.google.com/maps/place/{LONG}+{LAT}/"

  print("LOCATION ---->",url)

  quit()







payload={}

headers = {

"x-api-key": "API"

}



ip = sys.argv[2]



print(Fore.GREEN + ''' 

                               /T /I

                              / |/ | .-~/

                          T\ Y  I  |/  /  _

         /T               | \I  |  I  Y.-~/

        I l   /I       T\ |  |  l  |  T  /

     T\ |  \ Y l  /T   | \I  l   \ `  l Y

 __  | \l   \l  \I l __l  l   \   `  _. |

 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |

  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |

.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./

 >--.  ~-.   ._  ~>-"    "\\   7   7   ]

^.___~"--._    ~-{  .-~ .  `\ Y . /    |

 <__ ~"-.  ~       /_/   \   \I  Y   : |

   ^-.__           ~(_/   \   >._:   | l______

       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.

              (_/ .  ~(   /'     "~"--,Y   -=b-. _)

               (_/ .  \  :           / l      c"~o \

                \ /    `.    .     .^   \_.-~"~--.  )

                 (_/ .   `  /     /       !       )/

                  / / _.   '.   .':      /        '

                  ~(_/ .   /    _  `  .-<_

                    /_/ . ' .-~" `.  / \  \          ,z=.

                    ~( /   '  :   | K   "-.~-.______//

                      "-,.    l   I/ \_    __{--->._(==.

                       //(     \  <    ~"~"     //

                      /' /\     \  \     ,v=.  ((

                    .^. / /\     "  }__ //===-  `

                   / / ' '  "-.,__ {---(==-

                 .^ '       :  T  ~"   ll       

                / .  .  . : | :!        \\

               (_/  /   | | j-"          ~^

                 ~-<_(_.^-~"

''')



if "-o" in sys.argv:

  file = open("output.txt", "w")



  response = requests.get(f"http://who.is/whois-ip/ip-address/{ip}")



  soup = BeautifulSoup(response.content, 'html.parser')



  pre_tag = soup.find('pre')



  print(pre_tag.text.strip(), file=file)



  print("\n__________________________LOCATION__________________________\n", file=file)



  print(f"--> https://db-ip.com/{ip}", file=file)



  print("\n__________________________SOME MORE INFO__________________________\n", file=file)



  url = f"https://api.criminalip.io/v1/ip/data?ip={ip}&full=true"

  url = f"https://api.criminalip.io/v1/ip/data?ip={ip}"



  response = requests.request("GET", url, headers=headers, data=payload)



  json_response = json.loads(response.text)

  print(json.dumps(json_response, indent=2), file=file)

  if "-S" in sys.argv:

      url = f"https://api.criminalip.io/v1/ip/summary?ip={ip}"

      

      response = requests.request("GET", url, headers=headers, data=payload)

      print("\n__________________________SUMMARY__________________________\n", file=file)

      print(response.text, file=file)



  if "-V" in sys.argv:

      url = f"https://api.criminalip.io/v1/ip/vpn?ip={ip}"

      

      response = requests.request("GET", url, headers=headers, data=payload)

      print("\n__________________________VPN__________________________\n", file=file)

      print(response.text, file=file)





  if "-H" in sys.argv:

      url = f"https://api.criminalip.io/v1/ip/hosting?ip={ip}"

      

      response = requests.request("GET", url, headers=headers, data=payload)

      print("\n__________________________HOSTING__________________________\n", file=file)

      print(response.text, file=file)



  if "-M" in sys.argv:

      url = f"https://api.criminalip.io/v1/ip/malicious-info?ip={ip}"

      

      response = requests.request("GET", url, headers=headers, data=payload)

      print("\n__________________________MALICIOUS-INFO__________________________\n", file=file)

      print(response.text, file=file)



  if "-P" in sys.argv:

      url = f"https://api.criminalip.io/v1/ip/privacy-threat?ip={ip}"

      

      response = requests.request("GET", url, headers=headers, data=payload)

      print("\n__________________________PRIVACY-THREAT__________________________\n", file=file)

      print(response.text, file=file)



  if "-Safe" in sys.argv:

      url = f"https://api.criminalip.io/v1/ip/is_safe_dns_server?ip={ip}"

      

      response = requests.request("GET", url, headers=headers, data=payload)

      print("\n__________________________IS-SAFE-DNS-SERVER__________________________\n", file=file)

      print(response.text, file=file)

  print("Output Saved!")

else:

  response = requests.get(f"http://who.is/whois-ip/ip-address/{ip}")



  soup = BeautifulSoup(response.content, 'html.parser')



  pre_tag = soup.find('pre')



  print(pre_tag.text.strip())



  print("\n__________________________LOCATION__________________________\n")



  print(f"--> https://db-ip.com/{ip}")



  print("\n__________________________SOME MORE INFO__________________________\n")



  url = f"https://api.criminalip.io/v1/ip/data?ip={ip}&full=true"

  url = f"https://api.criminalip.io/v1/ip/data?ip={ip}"



  response = requests.request("GET", url, headers=headers, data=payload)



  json_response = json.loads(response.text)

  print(json.dumps(json_response, indent=2))



  if "-S" in sys.argv:

    url = f"https://api.criminalip.io/v1/ip/summary?ip={ip}"

    

    response = requests.request("GET", url, headers=headers, data=payload)

    print("\n__________________________SUMMARY__________________________\n")

    print(response.text)



  if "-V" in sys.argv:

    url = f"https://api.criminalip.io/v1/ip/vpn?ip={ip}"

    

    response = requests.request("GET", url, headers=headers, data=payload)

    print("\n__________________________VPN__________________________\n")

    print(response.text)





  if "-H" in sys.argv:

    url = f"https://api.criminalip.io/v1/ip/hosting?ip={ip}"

    

    response = requests.request("GET", url, headers=headers, data=payload)

    print("\n__________________________HOSTING__________________________\n")

    print(response.text)



  if "-M" in sys.argv:

    url = f"https://api.criminalip.io/v1/ip/malicious-info?ip={ip}"

    

    response = requests.request("GET", url, headers=headers, data=payload)

    print("\n__________________________MALICIOUS-INFO__________________________\n")

    print(response.text)



  if "-P" in sys.argv:

    url = f"https://api.criminalip.io/v1/ip/privacy-threat?ip={ip}"

    

    response = requests.request("GET", url, headers=headers, data=payload)

    print("\n__________________________PRIVACY-THREAT__________________________\n")

    print(response.text)



  if "-Safe" in sys.argv:

    url = f"https://api.criminalip.io/v1/ip/is_safe_dns_server?ip={ip}"

    

    response = requests.request("GET", url, headers=headers, data=payload)

    print("\n__________________________IS-SAFE-DNS-SERVER__________________________\n")

    print(response.text)

