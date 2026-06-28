#!/usr/bin/env python3
"""
Generate ElevenLabs narration for chapters from Swimming in a New Ocean.

Usage:
    pip install requests
    python narrate_chapters.py

Outputs MP3 files into an audio/ directory.
"""

import requests
import os

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "WsPXzUoQ9wMYrz5cJnBS"
URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

HEADERS = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY,
}

CHAPTERS = {
    "chapter_1_opening": {
        "title": "Swimming in a New Ocean — Opening",
        "text": """The invitation back felt like a homecoming. After the sustained emergency of COVID response — the data sprints, the incident command structures, the strange intimacy of a public health system under pressure — returning to communicable disease seemed like solid ground. Familiar work. Work I knew how to do.

But something had shifted, and it took me a while to name it.

I kept looking at the data and seeing the shape of the outcomes before I ran the analysis. Not because the pathogen was predictable, but because the people most affected were not random. They were patterned — by neighborhood, by occupation, by the particular exhaustion that comes from housing insecurity or working without sick leave. The surveillance numbers were telling me something the case definitions weren't designed to capture.

This is not a novel observation in public health. We have known for a long time that zip code predicts health outcomes better than genetic code. But there's a difference between knowing something academically and watching it move through your data in real time, shaping the very metrics you've been handed responsibility for. The honest question I found myself sitting with was: what exactly am I measuring, and what am I leaving out by measuring it this way?"""
    },
    "chapter_2_paradigm_problem": {
        "title": "The Paradigm Problem",
        "text": """The Paradigm Problem.

Mervyn Susser saw this coming.

Writing in the mid-1990s with his son Ezra, Susser argued that the dominant paradigm of his era — risk factor epidemiology — was growing less serviceable. It had done extraordinary work. The identification of individual-level risk factors had reshaped medicine and public health across the second half of the twentieth century. But the paradigm had a ceiling. By focusing relentlessly on proximate causes at the individual level, it left systematically understudied the forces acting at other levels — social, environmental, structural — that determined why some people were exposed to risk in the first place and others were not.

Susser called what he saw coming eco-epidemiology. The image he reached for was Chinese boxes — nested levels of organization, each containing the one below it, each requiring its own methods and its own questions. Molecular epidemiology at the innermost level. Individual risk factors in the middle. Social and environmental contexts at the outermost ring. The argument was not that risk factors didn't matter. It was that a single-level paradigm, however well executed, could not see the whole problem. The web of causation had a spider, and risk factor epidemiology wasn't looking for it.

What Susser described as an intellectual limitation of the paradigm, I kept recognizing as an institutional one. Applied public health had inherited a siloed structure from the disciplines that preceded it. Programs organized around disease categories. Data systems organized around programs. Funding organized around data systems. Each level optimized for its own outputs, accountable to its own metrics, largely incurious about what was happening one box out.

The result was a kind of enforced myopia. Not malicious — institutional myopia rarely is. But consequential. The Arant and Rosen study had made the court system's role in viral suppression visible in the data. But the data was only telling part of the story. I had seen another part of it through my time working with the state's AIDS Drug Assistance Program, known as HMAP. Jails across North Carolina had various arrangements in place to bridge medications for people entering custody. Some were thoughtful and well-coordinated. Others were not. The continuity of antiretroviral therapy — the thing that produces and sustains viral suppression — depended on arrangements that were locally negotiated, inconsistently implemented, and largely invisible to the surveillance system tracking the outcome.

There was something else I had learned, through Dr. Michelle Ogle — a clinician and former member of the Presidential Advisory Council on HIV/AIDS — about what sustaining suppression actually requires at the level of the body and the life. Antiretroviral medications need to be taken with food. Not as a preference, but as a clinical necessity — absorption, tolerability, adherence. Dr. Ogle's practice had recognized that prescribing the medication was not enough. They installed a food pantry. Not as a charitable gesture, but as a clinical intervention. Food is medicine. And medicine that is taken regularly, with adequate nutrition, produces viral suppression. Viral suppression is prevention. The dividend — the reduction in transmission, the sustained health of the patient, the cost avoided downstream — is real and measurable. But it only appears when the system is designed to maximize health outcomes rather than simply to deliver a prescription.

What the surveillance metric recorded was the outcome. What it could not see was the food pantry, the jail medication bridge, the broken appointment, the lapsed insurance. A communicable disease branch measuring suppression rates was measuring the shadow of a system it couldn't see. Susser would have recognized the problem immediately. The outcome lived at one level. The causes lived in the boxes surrounding it.

Susser's prescription was integration — not the dissolution of levels, but the explicit recognition of their connections and a commitment to designing research and practice that could move between them. That is harder than it sounds in a system that funds silos, staffs silos, and measures the outputs of silos. The Chinese boxes are real. But the walls between them are largely institutional, not epidemiological. They reflect how we organized ourselves, not how disease actually moves through the world.

This was the tension I kept returning to. Not just in the data. In the architecture of the field itself."""
    }
}

PRONUNCIATION_SUBS = {
    "Susser": "Suhsser",
    "Arant": "Arrant",
    "HMAP": "eighchmap",
}

def prepare_text(text):
    for word, replacement in PRONUNCIATION_SUBS.items():
        text = text.replace(word, replacement)
    return f"<speak>{text}</speak>"

os.makedirs("audio", exist_ok=True)

for filename, chapter in CHAPTERS.items():
    print(f"Generating: {chapter['title']}...")
    response = requests.post(
        URL,
        json={
            "text": prepare_text(chapter["text"]),
            "model_id": "eleven_flash_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0.3,
                "use_speaker_boost": True,
                "speed": 1.1,
            }
        },
        headers=HEADERS,
        timeout=120,
    )
    if response.status_code == 200:
        out_path = f"audio/{filename}.mp3"
        with open(out_path, "wb") as f:
            f.write(response.content)
        print(f"  Saved: {out_path} ({len(response.content) // 1024} KB)")
    else:
        print(f"  Error {response.status_code}: {response.text}")

print("Done.")
