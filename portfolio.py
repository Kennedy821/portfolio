import streamlit as st
from streamlit.components.v1 import html as st_html
from textwrap import dedent


# adding in some functions 
import base64, mimetypes, pathlib

def img_to_data_uri(path: str | pathlib.Path) -> str:
    """
    Read *path* (PNG, JPG, GIF, …) and return
    'data:<mime>;base64,<very-long-string>'.
    """
    path = pathlib.Path(path)
    mime = mimetypes.guess_type(path)[0] or "image/png"
    data = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{data}"

st.set_page_config(page_title="Timeline w/ Logos", layout="wide")



# this is the code for the header: 

PROFILE_PIC = img_to_data_uri("vb_pitch_photo.png")  
email = st.secrets['email'] 
linkedin_url = st.secrets['linkedin_url']
github_url = st.secrets['github_url_1']
github_url_2 = st.secrets['github_url_2']
medium_url = st.secrets['medium_url']

SOCIALS = [
    {"icon": "fab fa-linkedin-in", "url": linkedin_url},
    {"icon": "fab fa-github",      "url": github_url},          # GitHub #1
    {"icon": "fab fa-github",      "url": github_url_2},     # GitHub #2
    {"icon": "fab fa-medium",      "url": medium_url},
    {"icon": "fa-solid fa-envelope","url": f"mailto:{email}"}, 
]

# ----------  CSS  ----------------------------------------------------
css_header = dedent("""
<link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  .hero      {display:flex;align-items:center;gap:40px;margin:2rem 0 3rem;}
  .hero-img  {width:260px;height:260px;border-radius:50%;object-fit:cover;
              box-shadow:0 2px 6px rgba(0,0,0,.15);}
  .hero-text h1 {margin:0;font-size:3.2rem;font-weight:600;color:#404040;}
  .hero-text p  {margin:.4rem 0 1.2rem;font-size:1.4rem;color:#6a6a6a;}
  .hero-icons a {display:inline-flex;align-items:center;justify-content:center;
                 width:44px;height:44px;margin-right:10px;border-radius:80%;
                 background:#1a1a1a;color:#fff;font-size:1.6rem;
                 transition:background .2s ease;}
  .hero-icons a:hover {background:#444;}
  @media(max-width:600px){
     .hero      {flex-direction:column;text-align:center;}
     .hero-img  {width:200px;height:200px;}
     .hero-icons a{width:48px;height:48px;margin-right:6px;}
  }
</style>
""")

# ----------  assemble the icons  ------------------------------------
icons_html = "".join(
    f'<a href="{s["url"]}" target="_blank" rel="noopener"><i class="{s["icon"]}"></i></a>'
    for s in SOCIALS
)

# ----------  final header markup  -----------------------------------
header_html = f"""
<div class="hero">
   <img src="{PROFILE_PIC}" class="hero-img" alt="Me">
   <div class="hero-text">
       <h1>Tariro Mashongamhende</h1>
       <p>I use data science and spatial analysis to build cool things for people to use 🌎⚡️🤖</p>
       <div class="hero-icons">
           {icons_html}
       </div>
   </div>
</div>
<hr>
"""

# ------------------------------------------------------------------------------------------------
# the code is below is for the timeline: 
# ------------------------------------------------------------------------------------------------





# ------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------
# 1)  DATA:  add an optional 'logo' key (local path or URL)
# --------------------------------------------------------------------
entries = [

    {
        "date": "2024 – 2025",
        "logo": img_to_data_uri("University_College_London_logo.png"),
        "html": """<p>
  Completed my MSc in
  <a href="https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-spatial-science-msc" target="_blank" rel="noopener">
    Urban Spatial (Data) Science
  </a>,
  formalising lots of the things I’d picked up over the years and learning some cool stuff.
  My thesis focused on the relations between image &amp; natural language in the context of land-cover and land-use dynamics, using deep-learning transformer models and was supervised by <a href="https://profiles.ucl.ac.uk/98496-claire-dooley" target="_blank" rel="noopener">Dr Claire Dooley </a>.
  Took some great modules with <a href="https://en.wikipedia.org/wiki/Hannah_Fry" target="_blank" rel="noopener">Professor Hannah Fry</a>, <a href="https://profiles.ucl.ac.uk/11266-michael-batty" target="_blank" rel="noopener">Professor Michael Batty</a> and  <a href="https://profiles.ucl.ac.uk/31566-elsa-arcaute" target="_blank" rel="noopener">Professor Elsa Arcaute </a>.
  I also helped out at the leading Urban Planning and Management conference
  (<a href="https://cupum.co/" target="_blank" rel="noopener">CUPUM</a>) held in London at UCL East.
  Selected for UCL’s
  <a href="https://www.ucl.ac.uk/enterprise/students/start-business-or-social-enterprise/venture-builder-turn-your-idea-reality" target="_blank" rel="noopener">
    Venture Builder Programme
  </a>
  and took part in hackathons like
  <a href="https://www.aienginehackathon.com/" target="_blank" rel="noopener">AI Engine</a>,
  building projects with tools from
  <a href="https://openai.com/" target="_blank" rel="noopener">OpenAI</a>,
  <a href="https://www.anthropic.com/" target="_blank" rel="noopener">Anthropic</a>,
  <a href="https://deepmind.google/models/gemini/" target="_blank" rel="noopener">Google Gemini</a>,
  <a href="https://mistral.ai/" target="_blank" rel="noopener">Mistral</a>,
  and
  <a href="https://elevenlabs.io/" target="_blank" rel="noopener">ElevenLabs</a>.
</p>

<p>
    <img src="https://github.com/Kennedy821/portfolio/blob/9db5b145e614d67a220ef19a5f804a8cb3d7e220/UCL_images.png?raw=1" alt="UCL Images">
</p>"""

        # "images": img_to_data_uri("UCL_images.png")
    },
    {
        "date": "2016 – 2024",
        "logo": img_to_data_uri("pwc_and_strategyand_logo.png"),
        "html": """<p>
  Worked as a
  <a href="https://www.strategyand.pwc.com/uk/en.html" target="_blank" rel="noopener">
    consultant &amp; data scientist
  </a>
  across sectors, focusing on strategy projects in TMT, Retail, and Financial Services.
  Built a geospatial team and an industry-leading geospatial location-intelligence platform,
  and supported other teams as the UK geospatial SME.
  Collaborated with telecommunications companies and banks to develop their data products.
  Traveled around the country and got to see some impressive technology and places along the way.
</p>"""
    },
    {
        "date": "2012 – 2016",
        "logo": img_to_data_uri("exeter_uni_new_logo.png"),
        "html": """<p>
  Completed an undergraduate degree in
  <a href="https://www.exeter.ac.uk/study/undergraduate/courses/business/businessman/" target="_blank" rel="noopener">
    Business and Management
  </a>
  with Industrial Experience. Got interested in urban systems, business and economic history, and developed my first start-up idea. My thesis focused on a comparative assessment of the growth of megacities during the 18<sup>th</sup> and 19<sup>th</sup> centuries. Met and worked with
  <a href="https://experts.exeter.ac.uk/3429-david-boughey" target="_blank" rel="noopener">
    Professor David Boughey
  </a>, who also supervised my thesis.
</p>

<p>
  Worked with the
  <a href="https://business-school.exeter.ac.uk/careers/" target="_blank" rel="noopener">
    Business School Careers team
  </a>
  to help students secure graduate jobs, supported employers in targeting the right student cohorts for their businesses, and organised site visits to the Business School.
</p>

<p>
  Took a year out to work in PwC’s Strategy &amp; Economics team, where I first became involved in spatial analysis—helping organisations with their contingency planning using gravity models and assisting government with regional economic-development plans.
</p>"""
    },
    # ...add more...
]




# --------------------------------------------------------------------
# 2)  CSS:  dot + logo column + content column
# --------------------------------------------------------------------
css = dedent("""
<style>
    body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  .tl-wrapper{position:relative;margin:2rem auto;width:100%;padding-bottom:3rem;}
  .tl-wrapper::before{content:'';position:absolute;left:120px;top:0;bottom:0;width:2px;background:#d0d0d0;}
  .tl-item{display:flex;gap:20px;margin-bottom:2.5rem;}
  .tl-date{width:100px;text-align:right;font-weight:600;padding-right:20px;color:#959595;}
  .tl-dot{min-width:12px;height:12px;background:#b5b5b5;border-radius:50%;margin-top:6px;}
  .tl-logo img{width:72px;height:72px;object-fit:contain;border-radius:6px;box-shadow:0 1px 4px rgba(0,0,0,.1);}
  .tl-logo{display:flex;align-items:flex-start;}
  .tl-content{flex:1;line-height:1.5;color:#111;}
  /* Mobile tweaks */
  @media (max-width:640px){
     .tl-wrapper::before{left:80px;}
     .tl-date{width:60px;font-size:.8rem;}
     .tl-logo img{width:56px;height:56px;}
  }
</style>
""")

# --------------------------------------------------------------------
# 3)  HTML assembly
# --------------------------------------------------------------------
# html_bits = ["<div class='tl-wrapper'>"]
# for item in entries:
#     html_bits.append(f"""
#       <div class='tl-item'>
#         <div class='tl-date'>{item["date"]}</div>
#         <div class='tl-dot'></div>
#         <div class='tl-logo'><img src="{item["logo"]}" alt=""></div>
#         <div class='tl-content'>{item["html"]}</div>
        
#       </div>
#     """)

# html_bits.append("</div>")


# this is an alternative version with images included for each section
counter = 0
html_bits = ["<div class='tl-wrapper'>"]
for item in entries:
    if counter == 0:
        html_bits.append(f"""
        <div class='tl-item'>
            <div class='tl-date'>{item["date"]}</div>
            <div class='tl-dot'></div>
            <div class='tl-logo'><img src="{item["logo"]}" alt=""></div>
            <div class='tl-content'>{item["html"]}</div>
            
        </div>
        """)
    else:
        html_bits.append(f"""
        <div class='tl-item'>
            <div class='tl-date'>{item["date"]}</div>
            <div class='tl-dot'></div>
            <div class='tl-logo'><img src="{item["logo"]}" alt=""></div>
            <div class='tl-content'>{item["html"]}</div>            
        </div>
        """)
    counter += 1
html_bits.append("</div>")

# --------------------------------------------------------------------
# 4)  Render
# --------------------------------------------------------------------
# st_html(css + "".join(html_bits), height=1000, scrolling=True)

timeline_html = css + "".join(html_bits)
full_page = css_header + header_html + timeline_html   # <- timeline_html comes from before

st_html(full_page, height=1200, scrolling=True)

st.markdown("---")
st.header("Projects")

# project 1 - Project Infinite
col1,col2,col3, col4 = st.columns([0.5,2,9,0.5])
with col1:
    pass
with col2:
    st.image(img_to_data_uri("project_infinite_logo.png"))
with col3:
    st.markdown("**Project Infinite**")
    st.text("""Project Infinite is an attempt at building a self-perpetuating living sandbox where agents (driven largely by large-language-models) think, remember and act inside a shared fictional world. The population, geography and lore grow or fade on their own, so every visit uncovers new alliances, conflicts and myths that no one scripted. All you need to do is create a high-level brief (or not we can make a random one for you) and press play, and watch the story write itself.""")
with col4:
    pass

# project 2 - PSIL
col1,col2,col3, col4 = st.columns([0.5,2,9,0.5])
with col1:
    pass
with col2:
    st.image(img_to_data_uri("psil_screengrab.png"))
with col3:
    st.markdown("**[PSIL](https://psilproject.streamlit.app/psil_login)**")
    st.markdown("""
            Started off as a quick way to get better recommendations and quickly turned into a multi-year project. [PSIL (Predict Songs I Like)](https://psilproject.streamlit.app/psil_login) is a sound based similarity search and recommendation engine using Network Science and Machine Learning. Users can upload songs or type / speak what kind of music their listening to and get some recommendations.
            """)
with col4:
    pass

# project 3 - Notebot
col1,col2,col3, col4 = st.columns([0.5,2,9,0.5])
with col1:
    pass
with col2:
    st.image(img_to_data_uri("notebot_detailed_notes_screengrab.png"))
with col3:
    st.markdown("**Notebot**")
    st.markdown("""
            I built [Notebot](https://notebot.streamlit.app/notebot_login) initially as a way to work productively while doing my MSc. It has three components, a transcription part, a summarisation part and a quiz section made up of open or multiple choice questions. The notes can be generated at a granular as well as high-level. My favourite bit is to speak to Notebot and go through specific course content almost like office hours with an infinitely patient professor. I found it very good for active learning as well as for generating audio files for me to listen to on the trains back home.
            """)
with col4:
    pass


# project 4 - Election Slugbot
col1,col2,col3, col4 = st.columns([0.5,2,9,0.5])
with col1:
    pass
with col2:
    st.image(img_to_data_uri("election_slugbot_screengrab.png"))
with col3:
    st.markdown("**Election Slugbot**")
    st.markdown("""
                [Election Slugbot](https://projectelectionslugbot.streamlit.app/) started as a playful experiment in predicting the UK’s 2024 general election using modern machine learning techniques and location-based data, rather than traditional polls. Polls aren’t inherently bad but relying solely on them feels a bit dated, especially when we have powerful language models and abundant data at our fingertips. So, could we predict election results without polling at all?

                Turns out that you can (in the most part). Using past voting patterns and some quick-and-dirty ML models, Election Slugbot generated impressive  headline seat predictions, even matching the official exit poll pretty closely in one case. It wasn’t perfect, particularly when drilling down to seat-level details, nonetheless, it demonstrates that even a straightforward ML approach can rival traditional polling. A flawed yet promising glimpse into how elections might be forecasted differently in the future.            """)
with col4:
    pass

# project 4 - STP
col1,col2,col3, col4 = st.columns([0.5,2,9,0.5])
with col1:
    pass
with col2:
    st.image(img_to_data_uri("stp_actual_app_screengrab.png"))
with col3:
    st.markdown("**STP**")
    st.markdown("""
            Like many people I developed a plant habit during the pandemic and soon reached a point where it was hard to remember which plants had been watered when. I built [Save this Plant (STP)](https://savethisplantbeta.streamlit.app/) to act as a plant watering diary app but I soon added in some cool features like plant specific deep learning models that would tell me when I should probably water a plant i.e. in a couple of days water your snake plant. It’s been deprecated as unfortunately due a melted logic board which meant I lost all my application preprocessing code and backups. Here's the [repo](https://github.com/Kennedy821/save_this_plant) if anyone is looking for inspiration.
             Maybe one day I’ll bring it back.
            """)
with col4:
    pass



st.markdown("---")
st.header("Articles & Blogs")
st.markdown(" * Here is an article on how to use LLMs to predict an [election outcome](https://tariromashongamhende.bearblog.dev/blog/)")
st.markdown(" * An in-depth blog on using machine learning, one or two raspberry pi computers and some sensors to have healthier and happier plants using the [STP project](https://medium.com/@tk_m/save-this-plant-the-future-of-amateur-plant-care-b92549dd71f5/)")
st.markdown(" * An article published in the Undergraduate Exeter Academic Journal on the impact of double taxation told through the story of the [Carlton Hotel](https://www.linkedin.com/pulse/tale-two-taxes-story-carlton-hotels-south-africa-ltd-mashongamhende?trackingId=hhzomStvRuuiZRt5VVCanw%3D%3D&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_recent_activity_content_view%3BC%2Fvf4n69TeqHOPzGmlqmMw%3D%3D/) in South Africa back in the 1900s")





