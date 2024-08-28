from services.serp_api_service import get_academic_info
from services.openai_service import generate_response
from textwrap import wrap

def generate_research_letter(name, prof_name, university, model, special_pref, resume):
    N = 10
    academic_info = get_academic_info(prof_name, university, N)
    if not academic_info:
        return None

    oppo = "research opportunities/online research assistant opportunity/research internship"
    time = "from June to September, 2024"
    funding = "do not need funding support"
    work_style = "in person/online/both"

    system_prompt = f"""
    Input: Information about my resume and the professor
    Output: A quality letter to ask Professor {prof_name} for {oppo} over {time} 

    Take a deep breath. Keep it Concise & Focus on Research Potential

    Your task is to write an email to introduce the me, {name}, to professor {prof_name} to get {oppo}. I {funding}. I will be available {time}. I am willing to work {work_style}. Show these information in the email. 

    You will be provided with the student’s resume and information about the professor. Analyze the research potential, academic skills, and unique qualities. Think step by step and analyse carefully. 

    Importance rank: 
    Research experiences & potential: 70%,
    Academic & technical skills: 25% [eg, technical internship/coding skills/analytical skills/modelling skills/past competition results and etc.]; 
    Unique qualities[eg. communication/leadership/responsibility]: 5% - one or two sentences are enough.

    Write the email in an inviting way to showcase the research potential of the student and how it fits/aligns with the professor’s research focus. Extract the most competitive and the most fit experience and analyse in priority. Write in good detail and structure. 

    Things to note when writing the email. {special_pref}
    """

    user_prompt = f"Here’s the publications by Professor {prof_name} from {university}: {academic_info} \n Here's my resume: {resume}"

    letter_1, _ = generate_response(system_prompt, user_prompt, model)
    letter_1 = format_paragraphs(letter_1)
    letter_2, _ = generate_response(system_prompt, user_prompt, model)
    letter_2 = format_paragraphs(letter_2)
    
    return letter_1, letter_2

def format_paragraphs(text, width=80):
    paragraphs = text.split('\n')
    formatted_paragraphs = []
    for paragraph in paragraphs:
        lines = wrap(paragraph, width)
        formatted_paragraphs.append('<p>{}</p>'.format('</br>'.join(lines)))
    return ''.join(formatted_paragraphs)
