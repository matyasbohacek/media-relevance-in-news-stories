
EX_0 = [
    "Haiti violence: Haiti gangs demand PM resign after mass jailbreak",
    """Haiti's government declared a 72-hour state of emergency on Sunday after armed gangs stormed a major prison. At least 12 people were killed and about 3,700 inmates escaped in the jailbreak.
Gang leaders are demanding the resignation of Prime Minister Ariel Henry, whose whereabouts are unknown since he travelled to Kenya.
Gangs control around 80% of the capital, Port-au-Prince.
Gang violence has plagued Haiti for years.
A government statement said two prisons - one in Port-au-Prince and the other in nearby Croix des Bouquets - were stormed over the weekend.
It said the acts of "disobedience" were a threat to national security and said it was instituting an immediate night-time curfew in response, which started at 20:00 local time (01:00 GMT on Monday).
Haitian media reported that police stations were attacked, distracting authorities before the coordinated assault on the jails.
Speaking to the BBC from Haiti, Serge Dalexis from the International Rescue Committee said that many police stations were under gang control on Friday, with "many police killed over the weekend".
Among those detained in Port-au-Prince were suspects charged in connection with the 2021 killing of President Jovenel Moïse.
Gang violence has further escalated since his assassination in 2021. Mr Moïse has not been replaced and presidential elections have not been held since 2016.
""",
    "/Users/matyasbohacek/Downloads/Example Data/video.mp4",
    "/Users/matyasbohacek/Downloads/Example Data/video.mp4",
    "people fleeing violence",
]

EX_1 = [
    "UK to finish with coal power after 142 years",
    """The UK is about to stop producing any electricity from burning coal - ending its 142-year reliance on the fossil fuel.
The country's last coal power station, at Ratcliffe-on-Soar, finishes operations on Monday after running since 1967.
This marks a major milestone in the country's ambitions to reduce its contribution to climate change. Coal is the dirtiest fossil fuel producing the most greenhouse gases when burnt.
Minister for Energy Michael Shanks said: "We owe generations a debt of gratitude as a country."
The UK was the birthplace of coal power, and from tomorrow it becomes the first major economy to give it up.
"It's a really remarkable day, because Britain, after all, built her whole strength on coal, that is the industrial revolution," said Lord Deben - the longest serving environment secretary.
The first coal-fired power station in the world, the Holborn Viaduct power station, was built in 1882 in London by the inventor Thomas Edison - bringing light to the streets of the capital.
From that point through the first half of the twentieth century, coal provided pretty much all of the UK’s electricity, powering homes and businesses.
In the early 1990s, coal began to be forced out of the electricity mix by gas, but coal still remained a crucial component of the UK grid for the next two decades.
In 2012, it still generated 39% of the UK's power.
""",
    "https://ichef.bbci.co.uk/news/1536/cpsprodpb/90f8/live/bb03ea20-7cdc-11ef-87ad-d7f77083c88b.jpg",
    "/Users/matyasbohacek/Downloads/Example Data/cropped.png",
    "The UK's last coal plant, Ratcliffe-on-Soar Power Station near Nottingham, ends operations on Monday",
]

CSS = """
html {
    background-color: #F5F5F2;
}

input.svelte-1mhtq7j.svelte-1mhtq7j.svelte-1mhtq7j:checked, input.svelte-1mhtq7j.svelte-1mhtq7j.svelte-1mhtq7j:checked {
    background-color: #499167;
    border-bottom-color: #499167;
    border-left-color: #499167;
    border-right-color: #499167;
    border-top-color: #499167;
    color: #499167;
}

input.svelte-1mhtq7j.svelte-1mhtq7j.svelte-1mhtq7j:checked, input.svelte-1mhtq7j.svelte-1mhtq7j.svelte-1mhtq7j:checked:hover {
    background-color: #499167;
    border-bottom-color: #499167;
    border-left-color: #499167;
    border-right-color: #499167;
    border-top-color: #499167;
    color: #499167;
}

.svelte-1gfkn6j {
    font-weight: bold !important;
}

gradio-app {
    background:  #F5F5F2 !important;
    background-color:  #F5F5F2 !important;
}

.prose h1 {
    color: #499167;
    font-size: 3em !important;
    margin-top: -20px;
}

gradio-app {
    background-color: #F5F5F2;
}

body, .gradio-container {
    background-color: #F5F5F2; /* Light mode background */
    color: #333333; /* Dark text color */
    font-family: Helvetica, Arial, sans-serif; /* Set font to Helvetica */
}

.built-with {
    display: none !important; /* Hide bottom panel */
}

.show-api {
    display: none !important; /* Hide bottom panel */
}

button, input, textarea, select {
    font-family: Helvetica, Arial, sans-serif; /* Ensure all inputs use Helvetica */
}

.gr-button {
    background-color: #357edd; /* Matte blue button background */
    color: white; /* White text for contrast */
    font-weight: bold; /* Bold font for buttons */
    border: none; /* Remove borders */
    border-radius: 4px; /* Slightly rounded corners for modern look */
}

.gr-button:hover {
    background-color: #78a498; /* Darker matte blue on hover */
}

.gr-textbox, .gr-slider, .gr-checkbox, .gr-dropdown {
    border: 1px solid #78a498; /* Matte blue borders */
    border-radius: 4px; /* Rounded corners */
}

.gr-title, .gr-subtitle {
    font-weight: bold; /* Bold titles */
    color: #78a498; /* Matte blue titles */
}

.container-spec {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: auto;
}

.assessment {
    padding: 20px;
    font-size: 1.2em;
    border-radius: 10px;
    color: white;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.relevant {
    background-color: #499167;
    color: #fff !important;
}

.not-relevant {
    background-color: #EE4266;
}

.check-mark {
    font-size: 2em;
}

.reasoning {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
}

.chat-button {
    height: 100% !important;
}
"""

LLM_PROMPT_ANALYSIS = (
    "You are evaluating the relevance and credibility of images and videos attached to news stories.\n"
    "Below, you will be presented with:\n"
    "- The title of the article\n"
    "- The article\n"
    "- The image caption, as presented in the article\n"
    "- Provenance metadata indicating source location and time, as well as edits made to the image\n\n"
    "Here is the data:\n"
    f"The title: $TITLE$\n"
    f"The body: $BODY$\n"
    f"Image caption: $IMAGE_CAPTION$\n"
    f"Provenance etadata: $METADATA$$\n"
    "Do not copy any data. Do the following. Analyze the following:\n"
    "1. Determine whether the location and time (year, month) when the media (images/videos) were taken is relevant to the news story.\n"
    "2. Determine if there was any tampering with the media (Photoshop edits, AI generation, etc.); resizing is okay.\n"
    "3. Based on the above, give one of the following assessments: 'RELEVANT' or 'NOT RELEVANT'\n"
    "Return your answer as a json/dictionary with the format: {'1-relevant': True/False, '1-reason': str, '2-relevant': True/False, '2-reason': str, '3-assessment': 'RELEVANT' / 'NOT RELEVANT'}\n"
    "No other text or commentary beyond the raw json, return raw json/dictionary. For strings, use double colon \" instead of single colon '."
)

LLM_PROMPT_FOLLOWUP_CHAT = "Here is your current reasoning: $CURRENT_REASONING$. Generate a verbose response to the following question, highlighting the importance of provenance metadata: $MESSAGE$"

OVERALL_ASSESSMENT_HTML_OUTPUT = """
    <div class="container-spec">
        <div id="overallAssessment" class="assessment $assessment_class$">
            <div style='color: #fff !important;'>$overall_assessment$</div><div class="check-mark"  style='color: #fff !important;'>$symbol$</div>
        </div>
        <div class="reasoning">
            <strong>Location and Source:</strong> <span>{"LOOKS GOOD " if $check_one$ else "MIGHT BE PROBLEMATIC "} <br><br> $reasoning_one$</span>
        </div>
        <div class="reasoning">
            <strong>Tampering:</strong> <span>{"LOOKS GOOD " if $check_two$ else "MIGHT BE PROBLEMATIC "} <br><br> $reasoning_two$</span>
        </div>
    </div>
"""

OVERALL_ASSESSMENT_OUTPUT = """
    Overall Assessment: $overall_assessment$
    Location and Source: {"LOOKS GOOD " if $check_one$ else "MIGHT BE PROBLEMATIC "} $reasoning_one$
    Tampering: {"LOOKS GOOD " if $check_two$ else "MIGHT BE PROBLEMATIC "} $reasoning_two$
    """