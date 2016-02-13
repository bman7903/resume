def Head():
  head = str( """ \
  <html><head><style>
  a {
     text-decoration: none;
     left-margin: 50px;
     left-padding: 50px;
     color: purple;
  }
  a:visited {
     text-decoration: none;
     color: green;
  }
  h1 {
    font-family: times;
    font-size: 100%;
  }
  h2  {
    font-family: times;
    margin: 10px;
    font-size: 100%;
  }
  h3  {
    font-family: times;
    margin: 30px;
    font-size: 100%;
  }
  h4  {
    font-family: times;
    left-margin: 50px;
    left-padding: 50px;
    font-size: 100%;
    display: inline;
    padding-left: 75px;

  }
  h5  {
    font-family: times;
    font-size: 100%;
    display: inline;
    padding-left: 75px;
    padding-right: 75px;
  }
  h6  {
    font-family: sans;
    text-align: right;
    font-size: 100%;
  }
  h7  {
    font-family: times;
    font-size: 24px;
    font-weight: bold;
    display: inline;
    display: inline-block;
    align-text: center;
  }
  h8 {
	font-family: cursive;
	font-size: 12px;
	font-style: normal;
	font-variant: normal;
	font-weight: 500;
	line-height: 26.4px;
  }

  hr { 
     border: 0;
     height: 1px; 
     background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); 
  }

  hr.style-three { 
     border: 0;
     margin: 1px;
     background: #999; 
  }

  hr.style-five { 
     border: 0; height: 0;
     box-shadow: 0 0 10px 1px black;
  } 
  hr.style-five:after {
     content: "\00a0";
  }

  hr.style-eight { 
     padding: 0; 
     border: none;
     border-top: medium double #333; 
     color: #333; 
     text-align: center; 
  }
  hr.style-eight:after {
     font-size: 100%;
     font-family: cursive;
     content: "James Bailey";
     display: inline-block; 
     position: relative; 
     top: -0.7em; font-size: 1.5em; 
     padding: 0 0.25em; 
     background: white; 
  }

  hr.style-nine { padding: 0; border: none; border-top: medium double #333; color: #333; text-align: center; } hr.style-nine:after { content: "James Bailey"; display: inline-block; position: relative; top: -0.7em; font-size: 1.5em; padding: 0 0.25em; background: white; }

  </style></head><body><h6>
  jb06732@gmail.com<br>
  415-272-4715</h6>
  <hr class="style-eight" \>""" )
  return head

def Intro( type, company ):
  def intro():
     itro = """<h2>To Whom it May Concern,<br></h2><h3>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;My name is James Bailey and I am currently looking to fill thirty hours a week working while I continue taking classes in IT at College of Marin. I have two more years of school ahead of me and would love to make more money with my spare time.  I am currently unavailable on Wednesday and Monday in the evening and afternoon but I otherwise have full availability.  I have an impeccable memory which lends its skills to multitasking, math, science, and people. I believe good leadership and teamwork  to be a crucial component to an efficient and happy work environment. I am a avid reader and a good listener.  I also enjoy hiking around Marins many beautiful trails.</h3>"""
     return itro
  def outro():
     otro = """<h2>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
               Drop me a line set up a interview.</h2>"""
     return otro
  tro = str( '%s\n%s' % ( intro(), outro() ) )
  return tro

def Exp():
  exp = \
  str( """<h5><hr \></h5><strong><center>Experience</center></strong><h1>
  <table><tr><td><h2><u>Rancho Shazzaam</u><lu>
  <h2><li>Greenbrae CA, Apt. Maintenence</li>
  <li>IT & cable and meneral maintenance</li></lu>
  &#172;&nbsp;&nbsp;<a href="http://www.sfgate.com/bayarea/article/GREENBRAE-S-RANCHO-SHAZAM-PUTS-AUTHORITIES-TO-THE-2907042.php">
  http://www.sfgate.com/bayarea/article/<br>GREENBRAE-S-RANCHO-SHAZAM-PUTS-AUTHORITIES-TO-THE-2907042.php</h2></a></td>
  <td>&emsp;</td><td> 5/11 - 7/14 </td><td>&emsp;</td></tr>

  <tr><td><u><h2>Finish carpentry</u><lu>
  <h2><li>Worked with a private contracter</li>
  <li>Remodeling, renovating, painting, new additions</li></lu>
  &#172;&nbsp;&nbsp;<a href="http://www.chaselawler.com">http://www.chaselawler.com</a></h2></td>
  <td>&emsp;</td><td> 6/11 - 1/13 </td><td>&emsp;</td><td>&emsp;</h2></td></tr>

  <tr><td><h2><u>Peets Coffee and Tea</u><lu>
  <h2><li>San Anselmo CA, Barista</li>
  <li>CRA Certified</li>
  <li>Opening barista</li></lu>
  &#172;&nbsp;&nbsp;<a href="http://www.peets.com">http://www.peets.com</a></h2></td>
  <td>&emsp;</td><td> 3/11 - 3/12 </td><td>&emsp;</h2></td></tr>

  <tr><td><h2><u>Michaan's Auction</u><lu>
  <h2><li>Alameda, California, Shlepper</li>
  <li>Recieving estates, truck runs, auction set up, photography assistance</li></lu>
  &#172;&nbsp;&nbsp;<a href="http://www.michaans.com">http://www.michaans.com</a></td>
  <td>&emsp;</td><td> 3/10 - 3/11 </td><td>&emsp;</h2></td></tr>

  <tr><td><h2><u>Wipe Out Bar and Grill</u><lu>
  <h2><li>Ross, California, Lead Server</li>
  <li>Serving, training, closing, setting example, early restaurant growth</li>
  <li>Tips Certified</li></lu>
  &#172;&nbsp;&nbsp;<a href="http://www.wipeoutbarandgrill.com">http://www.wipeoutbarandgrill.com</a></td>
  <td>&emsp;</td><td> 11/07 - 6/09 </td><td>&emsp;</h2></td></tr>

  <tr><td><h2><u>The Counter Burger</u><lu>
  <h2><li>Palo Alto, California, Supervisor</li>
  <li>Expo, host, server, to-go and bar, facilitate lunch shift change, count outs, training, early restaurant growth</li></lu>
  &#172;&nbsp;&nbsp;<a href="http://www.thecounterburger.com">http://www.thecounterburger.com</a></td>
  <td>&emsp;</td><td> 5/06 - 12/06 </td><td>&emsp;</h2></td></tr>

  <tr><td><h2><u>Environment California</u><lu>
  <h2><li>San Francisco, CA, Team Leader</li>
  <li>Fund raising, soft calling, site scouting, data basing, training</li></lu>
  &#172;&nbsp;&nbsp;<a href="http://www.environmentcalifornia.org">http://www.environmentcalifornia.org</a></td>
  <td>&emsp;</td><td> Summer 04/05 </td><td>&emsp;</h2></td></tr></table><h5><hr \></h5>""" )
  return exp

def Education():
  edu = \
  str( """ <strong><center>Education</strong></center>
  <center><table><tr><td>&emsp;<td> <u>School</u> </td><td> <u>Location</u> </td><td> <u>Date</u> </td><td> <u>Degree</u> </td><td>&emsp;</td></tr></center>
  <tr><td>&emsp;<td> San Andraes High </td><td> Larkspur </td><td> 2003 </td><td>  HSG </td><td>&emsp;</td></tr>
  <tr><td>&emsp;</td><td> National Bartenders </td><td> Mountan View </td><td> 2006 </td><td>  Mixology </td><td>&emsp;</td></tr>
  <tr><td>&emsp;</td><td> College of Marin </td><td> Kentfield </td><td> 2009 </td><td>  Pending </td><td>&emsp;</td></tr>
  <tr><td><h5><hr class="style-three" \></h5></td><td> &emsp; </td><td> <img src="http://fnord.crabdance.com/celtic.png"> </td><td> &emsp; </td><td> &emsp; </td><td><h5><hr class="style-three" \></h5></td></tr></table></center>""" )
  return edu

def Skills():
  skill = \
  str( """ <br><strong><center>Additional Skills</center></strong><table><tr><td>&emsp;&emsp;&emsp;</td><td><lu><h8>
  <li>Talented Barista</li>
  <li>CRA - Food Handlers Card</li>
  <li>I can juggle</li>
  <li>IT, Databasing, Web-Dev</li></lu></td></tr></table></h8>
  <h5><hr \></h5>""" )
  return skill

def Reffs():
  refs = str( """<center>Refferences available upon request</center><br></h1></body></html>""" )
  return refs

def Resume( type, company ):
  f = str( Head() )  
  n = str( Intro( type, company ) )
  o = str( Exp() )
  r = str( Education() + '\n' + Skills() )
  d = str( Reffs() )
  html = str( '%s\n%s\n%s\n%s\n%s' % ( f, n, o, r, d ) )
  return html

#g = Resume( 'one', 'two' )
#print g

