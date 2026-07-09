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

VOICE_SETTINGS = {
    "stability": 0.5,
    "similarity_boost": 0.75,
    "style": 0.3,
    "use_speaker_boost": True,
    "speed": 1.125,
}

CHAPTERS_ALL = {
    "chapter_1_the_homecoming": {
        "title": "Chapter I — The Homecoming",
        "text": """The invitation back felt like a homecoming. After the sustained emergency of COVID response — the data sprints, the incident command structures, the strange intimacy of a public health system under pressure — returning to communicable disease seemed like solid ground. Familiar work. Work I knew how to do.

But something had shifted, and it took me a while to name it.

I kept looking at the data and seeing the shape of the outcomes before I ran the analysis. Not because the pathogen was predictable, but because the people most affected were not random. They were patterned — by neighborhood, by occupation, by the particular exhaustion that comes from housing insecurity or working without sick leave. The surveillance numbers were telling me something the case definitions weren't designed to capture.

This is not a novel observation in public health. We have known for a long time that zip code predicts health outcomes better than genetic code. But there's a difference between knowing something academically and watching it move through your data in real time, shaping the very metrics you've been handed responsibility for. The honest question I found myself sitting with was: what exactly am I measuring, and what am I leaving out by measuring it this way?"""
    },
    "chapter_2_the_infrastructure": {
        "title": "Chapter II — The Infrastructure",
        "text": """The pandemic had forced us to confront this problem in real time. At scale, COVID broke person tracking almost immediately — the volume of tests flowing through surveillance systems outpaced our ability to reliably follow individuals across records. A person could appear multiple times, under slightly different identifiers, and the system had no reliable way to know it was looking at the same person twice. We had processes to clean this up for all of the reportable events — but the work fell onto expert hands dipping into the stream. Skilled people, doing careful work, one record at a time. It was not a scalable solution, and everyone knew it.

We worked with the health information exchange to implement a master-patient-index solution. It wasn't glamorous work, but it was foundational — the kind of infrastructure that makes everything else possible. The volumes of duplicate records were enormous. A person appearing multiple times under slightly different identifiers wasn't an edge case — it was the norm at pandemic scale. And buried within all of that were negative tests, which in surveillance terms are non-cases. A negative test tells you something clinically, but among case data it is noise — a nuisance that obscures the signal. There was no justification for pushing that burden onto users. The deduplication had to happen at the infrastructure level, invisibly, before the data ever reached the people trying to use it.

By reconciling lab tests and vaccine events to a consistent person-level record, we were able to support analyses that required knowing, with confidence, who had been vaccinated and who had subsequently tested positive. The solution was also capable of more targeted applications — school-based screening surveillance, for instance, had we needed to go there. Fortunately, we didn't. But the capability existed, and that mattered.

What that infrastructure sustained was an ongoing operation. Leading the COVID data team meant producing regular intelligence — situation reports, analytic summaries, and dashboards that needed to be accurate, current, and legible to a wide range of audiences. The public was the primary user. North Carolinians checking case counts, tracking hospitalizations, making decisions about their families and their lives. Behind them came epidemiologists, executive leadership, partner agencies, and the press. The COVID dashboard became one of the highest traffic assets the department had ever published — a daily point of contact between the public and the state's understanding of the epidemic. That visibility carried its own weight. The data had to be right, and it had to be right on time.<break time="0.5s" />

The work had different registers. Some of it fed partners and researchers who needed clean, reliable data to answer specific questions — long-form collaborations that took months to mature. But much of it was shorter order: quick analyses, rapid turnaround requests, the kind of work where someone needed an answer by the afternoon briefing and you figured out how to get there. We were running a kitchen that served both slow-cooked projects and short-order needs simultaneously, and the team had to be fluent in both.

External communications flowed through a dedicated comms team who translated what we produced into language and formats fit for public consumption and partner coordination. That boundary mattered — it let the data team stay close to the analysis while ensuring that what went out the door had been shaped for its audience.

And then there were the requests that arrived with a different kind of weight. Legal inquiries. Special requests that came flagged from above and needed handling with both speed and care. These were not uncommon, and they required a different kind of attentiveness — not just analytic rigor, but situational awareness about what was being asked, by whom, and why.

We did undertake some school-based screening work as well — applying the infrastructure we had built to support surveillance in educational settings during a particularly uncertain period of the response. The details of that work are not mine to share specifically, but the capability was real, and exercising it even in limited ways demonstrated something important: that the system could be pointed at new problems without being rebuilt from scratch.

That infrastructure made things possible that hadn't been possible before. The master-patient-index solution built with the health information exchange was not merely an operational fix — it was the prerequisite for a different kind of science. Because a person's record could now be held together reliably across data sources, it became possible to link COVID-19 surveillance data to the vaccine management system with the confidence that the matches were real. Working with colleagues at the UNC Gillings School of Global Public Health, that linked data became the foundation for a series of studies that would reach the highest levels of the scientific literature. By connecting North Carolina's COVID-19 surveillance system to the vaccine management system across more than ten million residents, we were able to answer questions the country was urgently asking. The first study, published in the New England Journal of Medicine, examined vaccine effectiveness across a nine-month period — tracking protection against infection, hospitalization, and death across all three available vaccines, and untangling how much of the summer 2021 surge was driven by waning immunity versus the emergence of the Delta variant. A second study, published in JAMA, examined how primary vaccination, booster doses, and prior infection each independently shaped a person's risk of severe outcomes. A third, back in the New England Journal of Medicine, looked specifically at bivalent boosters against severe Omicron infection — some of the earliest real-world evidence on the updated shots as they were being rolled out.

What I did not fully appreciate at the time was how much I was also learning about public health systems — not the data systems, but the organizational ones. Jessie Tenenbaum, the department's Chief Data Officer, had arrived from Duke before the pandemic began, bringing with her a vision that went beyond infrastructure. She was building toward something more ambitious: a learning public health system — one that could generate knowledge from its own operations, adapt in response to what it found, and share that learning across the institutions and communities it served. Working inside an organization she was helping to shape in that direction gave me a frame I didn't know I needed. The COVID response wasn't just an emergency. It was, if you were paying attention, a proof of concept.

What struck me was how much that work resembled the problem I kept seeing in HIV surveillance. The underlying challenge was the same: a person moving through systems that weren't designed to recognize them consistently over time. In COVID we had built something that could hold a person together across data sources. In HIV, we were still largely depending on systems that couldn't."""
    },
    "chapter_3_the_hiv_mirror": {
        "title": "Chapter III — The HIV Mirror",
        "text": """Work I'd been part of made this concrete in a way I couldn't look away from. A linkage study between statewide North Carolina criminal court records and confidential HIV surveillance data found that over 9,500 people with HIV experienced criminal charges during the study period, and those individuals were more likely to be male and report Black race. The research examined viral suppression — one of our clearest clinical markers of care continuity — in the twelve months before and after criminal charges, finding that the period following resolution of charges was associated with increased risk of falling out of suppression.

Read one way, that's a care gap. Read another way, it's a map of what the legal system does to a person's ability to stay healthy. The charges themselves were the exposure. The surveillance metric was just the evidence left behind.

But I kept pulling on another thread. My own work on HIV care outcome measures had surfaced a more fundamental problem with how we use registry-based data sources to tell the story of who is and isn't engaged in care. Surveillance systems depend on the ability to reconcile a person's records across time — to follow someone forward through the data as a continuous identity. When that reconciliation fails, when a name change, a document inconsistency, or an administrative gap breaks the chain, the system loses the person. Not because they stopped seeking care. Because the data couldn't hold them together.

There is a cruel irony embedded in this for HIV specifically. The U=U campaign — Undetectable equals Untransmittable — is one of the great public health messages of the modern era. It tells people living with HIV that sustained viral suppression protects not only their own health but that of their partners. But in the surveillance world, undetectable carries a different shadow meaning. A person who is virally suppressed may stop generating the lab events that make them visible in the data. They become, in a surveillance sense, untrackable. Undetectable equals untrackable. The very marker of treatment success becomes the mechanism by which the system loses the person — or mistakes their absence for disengagement.

The mechanism has echoes of immortal time bias — the person exists in the population, accumulating time at risk, but the surveillance system has lost the thread.

That loss doesn't look like a data quality problem. It looks like a lapse in care. It looks like disengagement. It looks, in the aggregate, like a disparity — one that points back at the patient rather than at the system doing the measuring.

This is where the social determinants stop being a background variable and start being a structural feature of the evidence itself. The populations most likely to experience document inconsistency over time — people who are incarcerated, people who are unhoused, people navigating systems that do not protect the stability of their identity — are the same populations whose outcomes we are most worried about. The surveillance gaps and the care gaps are not independent phenomena. They share a cause, and that cause lives upstream.

They are handed the conclusions — the disparity statistics, the engagement rates, the outcome dashboards — without the machinery behind them. They are not told that the gap the system sees may be partly a gap in the system's ability to see. It would shift accountability. It would demand a different kind of transparency from the institutions doing the measuring.

That's when the frame started to feel genuinely too small."""
    },
    "chapter_5_federal_and_national_stage": {
        "title": "Chapter V — The Federal and National Stage",
        "text": """This wasn't just a theoretical concern. I had the chance to bring it into a federal Technical Expert Panel convened to update the methods used to perform jurisdictional unmet need analyses — the estimates that tell a state or locality how many people with HIV are not receiving care, and that drive resource allocation decisions at the highest levels. These analyses depend heavily on surveillance data, which means they inherit all of its limitations. When records go unlinked, they don't disappear from the denominator. They accumulate there, quietly inflating the apparent size of the unmet need. The bias doesn't announce itself. It just creeps in one record at a time, until the estimate is carrying more noise than signal.

During a lunch break, David Holtgrave and I found ourselves in conversation about exactly this. Holtgrave had spent decades at the center of HIV prevention science — at CDC, at Johns Hopkins, on the President's Advisory Council — and he understood the methodological stakes as well as anyone. I walked him through what I was seeing: the ways that unlinked data was distorting the picture, and why the standard approaches weren't adequately accounting for it. By the end of the day, we had something practical to show for it. The panel dismissed with a plan to implement simple filters — guardrails designed to put reasonable limits on how much unlinked data could creep into the analysis and corrupt the signal.

It was not a dramatic solution. But it was the right one. Sometimes the most important methodological advance is the one that keeps a known bias from quietly compounding itself into a policy decision.

The federal TEP was one venue for this conversation. CSTE — the Council of State and Territorial Epidemiologists — was another. That particular meeting was being held in North Carolina, and its attendance carried its own unspoken weight. Several states had declined to send representatives, a quiet act of protest against the state's newly implemented HB2 legislation — a law that had drawn national condemnation for its restrictions on transgender individuals and its broader signal about who was welcome in public life. The irony was not lost on those of us in the room. A meeting convened to discuss the surveillance of a disease that had always disproportionately affected marginalized communities was being held in a state that had just legislated against one of them. Some of the people most essential to that conversation had stayed home.

Among those who came, however, I began to see the full landscape of how jurisdictions were responding to the same underlying problem, and what I found was both reassuring and troubling in equal measure. States were not ignoring the bias. They were working on it. But they were working on it independently, each developing their own local workaround to account for the distortion that unlinked records introduced into their HIV surveillance data.

I found myself calling this a Swiss cheese failure. Not because any single state's approach had holes — most of them were thoughtful and technically defensible — but because the system as a whole did. Each jurisdiction had developed its own patch for a gap that existed everywhere, and those patches didn't line up. The bias was being managed, but inconsistently, which meant that jurisdictional comparisons — the very comparisons that drive national resource allocation — were being made across data that had been filtered and adjusted in fundamentally different ways. You were no longer comparing like with like. You were comparing Swiss cheese to Swiss cheese, hoping the holes happened to fall in the same places.

What gave me some measure of hope was that states were already moving toward solutions. The conversation at CSTE was not one of denial but of shared recognition — a field beginning to coordinate around a problem it had long managed in isolation.

The CDC, to its credit, had already begun working on something more durable. The Black Box project — developed through Georgetown University with CDC support and eventually implemented across forty public health jurisdictions — was a direct response to exactly this problem. Its premise was straightforward but technically ambitious: create a secure, privacy-preserving intermediary that could receive HIV surveillance records from multiple jurisdictions, identify probable matches across state lines, and return those match probabilities back to each jurisdiction without ever exposing the underlying data.

The problem it was solving was real and growing. People with HIV are not stationary. They move across state lines for work, for family, for care. A jurisdiction-centric surveillance system, designed at a time when mobility was less of an assumption, was increasingly struggling to follow them. The result was duplicate records, inflated denominators, and distorted pictures of who was in care and who wasn't — compounding exactly the kind of bias we had been discussing. By the time of the CSTE meeting, the Black Box had processed millions of records across quarterly matching sessions, and jurisdictions covering three quarters of people living with diagnosed HIV in the United States had signed on.

It was, in other words, the infrastructure answer to the Swiss cheese problem. Not a local patch, but a shared solution. The kind that only becomes possible when a field stops managing a problem in isolation and starts naming it together."""
    },
    "chapter_6_the_platform_problem": {
        "title": "Chapter VI — The Platform Problem",
        "text": """And we needed to talk about the infrastructure we stood up to support the work. The current data platform was being marketed as a data lake — the image conjures something open, something that flows and connects, where tributaries find each other. What we actually had was something closer to a data silo in the cloud.

The distinction matters. Silos in the cloud still don't talk to each other. They're just higher up. And when I reached for the airplane analogy — which the image almost demands — it became clarifying rather than comforting. Planes at altitude, each in their own corridor, carefully managed not to collide. The entire system designed around separation. The culture that had grown up around this platform felt the same way: not collaborative by default, but compartmentalized by design, with coordination treated as an exception that required special permission rather than a baseline expectation.

You can't see the social determinants from inside a silo. You can't reconcile a person's records across systems that have been architected to stay apart. The platform was a symptom of something deeper — an institutional disposition toward protecting data boundaries rather than asking what becomes possible when you cross them carefully and responsibly.

There was another layer to this worth naming. The COVID-era data lake had genuinely good documentation — for the people already inside it. Operators could do their jobs. The machinery was legible to those who built it and maintained it. But for an outsider — a partner agency, a community organization, a researcher trying to understand what the data could actually answer — there was no real point of entry. No way to learn what was in there without already knowing someone who knew.

Local health departments experienced this in a concrete and consequential way. As the state developed cloud-based solutions for statewide COVID dashboards, local health departments did not get access to the granular data behind those dashboards. They received special reports and had opportunities to work with the team, but did not have many tools at their disposal. The decisions that shaped that access were made before those voices were fully heard. We do not know how hard they tried to request more. What we know is that the people coordinating access to testing and vaccines on the ground, fielding questions from communities navigating an unprecedented situation, and serving as trusted messengers who could respond to honest skepticism in ways that a statewide dashboard could not — those people were working with less than the situation warranted. They were the human layer of the response. And the data infrastructure, in some important respects, had outpaced them rather than equipped them.

If the data owners wanted storytelling, they had to start with metadata — a catalog, a data dictionary, some surface that an outsider could actually cling to. And if they wanted to signal that the data was open to collaboration, they needed mechanisms to do that intentionally. Not just access, but invitation. Not just infrastructure, but a posture toward the outside world that said: here is what we have, here is what it can do, and we want to work with you.

Without that, even a well-documented system becomes a closed system. The documentation serves the insiders. The outsiders never find the door.

It is worth noting that some infrastructure did exist between counties, the state, and external partners for special data sharing arrangements. There were genuine efforts to bridge gaps — including work to enhance HIV care data — but local solutions tended to be customized to a specific frame of reference, shaped by jurisdictional funding rather than interoperability. This is the nature of decentralized public health infrastructure: each jurisdiction builds what its funding and mandate allow, and the result is a landscape of locally coherent but globally fragmented solutions. Researchers who came prepared with a complete packet — operational requirements, data sharing agreements, data use agreements — could move faster, especially with leadership priority behind them.

Decentralization is not inherently a weakness. The weaving of local knowledge, local relationships, and local accountability into a larger system builds a kind of strength that top-down infrastructure rarely achieves. But that strength only arrives when the connections between the pieces are made under the right conditions — with shared purpose, adequate trust, and the scaffolding to hold it all together long enough to matter.

What made this particularly striking was the contrast with what we had just lived through: the COVID response had demonstrated that skilled coordination was possible — that data teams could move in concert, that information could flow across organizational boundaries when the stakes demanded it. But that coordination had not emerged from the platform. It had emerged from deliberate effort: stakeholder calls that kept everyone aligned, project management that tracked milestones, and legal reviews that gave the work its necessary blessing before it moved forward. Structure made it real. And structure like that has to be designed in — it does not arise on its own.

This is the part that bureaucratic solutions tend to get wrong. Silos are not an accident of bad intentions. They are the natural output of systems that optimize for control, compliance, and jurisdictional clarity. A data lake built inside that culture does not dissolve the silos. It relocates them.

This is precisely the problem that data-governance exists to address — not as a compliance-exercise, but as a framework for making intentional decisions about how data is shared, who has access, under what conditions, and toward what ends. Done well, data governance is the scaffolding that coordination requires. It holds the structure in place while the work gets built. Without it, even the most sophisticated infrastructure remains a collection of well-resourced but disconnected parts.

That, too, was part of what I was leaving."""
    },
    "chapter_11_a_prologue_still_being_written": {
        "title": "A Prologue Still Being Written",
        "text": """I remember the day he handed me a copy of his journal — opened to an article about developments in HIV surveillance. It was not an assignment. It was more like an offering. The kind of thing a mentor does when they see something in you before you see it in yourself. The article was nestled in an issue devoted to public health emergency preparedness — a collection that ranged across public health response, public communications, rural community preparedness, immunization information systems, and outbreaks. At the time, I read the HIV piece and moved on. I did not know then that I would spend the better part of the next decade working in exactly that field — or that nearly every other topic in that issue would become part of my professional life as well.

Lloyd died on August 26, 2025. He had only just stepped back from the journal he built.

What I did not fully appreciate until later was the quiet symmetry of that moment. Just weeks before his passing, our workgroup's article on behavioral health holds — using North Carolina's syndromic surveillance system to track patients boarding in emergency departments overnight while awaiting psychiatric care — was published in that same journal. The one he had handed me years earlier. The one he had spent three decades building into a home for exactly this kind of practice-grounded work.

I don't think Lloyd would have made much of the coincidence. He was too practical for that. But I find myself making something of it. The journal that first pointed me toward HIV surveillance ended up publishing work from the new ocean I had swum into. That feels like more than accident. It feels like the shape of a career that someone else could see before I could.

Dr. Anne Hakenewerth

Dr. Anne Hakenewerth was my mentor and my supervisor, and she was one of the rarest kinds of leaders I have encountered in this field — someone who could hold a genuinely full calendar and still make time for the kind of unhurried, practical conversation that actually changes how you think. Our offices shared a common wall, and I will admit that I learned more than a few things through that wall. Whether it was an epidemiological community of practice call or a tangle with an IT issue, she moved through both with the same grounded confidence. She too swam in deep waters, and she made it look natural.

Before I say what happened, I want to say what that season was. Working alongside colleagues in the communicable disease branch was one of the formative experiences of my professional life. We were there. We did our jobs. We figured out ways to make things work when the playbook didn't exist yet and the pressure was unrelenting. That branch was, for me, a genuine school of public health — not the credentialed kind, but the kind that comes from standing next to people who know things you don't and being trusted to figure out the rest. I am grateful for every one of those colleagues. I carry that season with me.

<break time="1.0s" />I have not fully processed her death. I am not sure I know how to.

We were walking to a meeting in another building — Anne a short distance ahead, myself and a small group about twenty seconds behind her — when she was struck by a car outside our office. The driver turned right on red without looking at the crosswalk. I moved without thinking. I helped her up from the ground and sat with her while she was disoriented, not because there was anything useful to say, but because sitting with someone matters. We didn't have many words between us. We made sure she was stable, that she was as okay as she could be, and we waited for the EMTs to arrive.

When the ambulance doors closed, I didn't know that Anne had suffered a brain bleed. I didn't know she would lose consciousness on the way to the hospital. I didn't know that what I had just witnessed on that sidewalk was the last time I would see her as herself. Our family and colleagues visited hers in the emergency department in the hours that followed. She never regained consciousness.

At the hearing for the defendant, Anne's daughter said something that has stayed with me: that her mother would have changed the shape of COVID response in North Carolina in ways we will simply never know. That is the particular cruelty of losing someone at the height of their capacity. The counterfactual is unresolvable. The absence has a shape, but no edges you can trace.

Anne was, in some way, a victim of a system out of tune. A crosswalk. A driver not looking. An infrastructure that had not kept pace with the people moving through it. Her death prompted the governor to direct the Department of Transportation to investigate pedestrian safety across the state. I attended a meeting of the Capitol Area Metropolitan Planning Organization to bring some light to the pedestrian hazards plaguing downtown Raleigh. Afterward, the DOT planner for the district — Joey Hopkins, who would later become Secretary of the Department — pulled me aside to describe plans already in motion: increased attentiveness measures, lane markings, improved turn signals, new signage. Small interventions. The kind that don't make headlines but do save lives.

There is something achingly familiar about that to anyone who works in public health. The upstream fix. The unglamorous infrastructure change. The reform that happens after someone is already gone.

There is no clean way to hold that.<break time="0.75s" /> I don't try to anymore.

What I can say is that the kind of public health she practiced — present, curious, connected to people, unafraid of the hard conversation — is the kind I am still trying to do. That is the only tribute that makes sense to me. Not words, but the work.

This piece is, in some sense, a downstream consequence of people like Lloyd and Anne — their investments in a younger analyst who didn't yet know where he was headed.<break time="0.5s" /> I am grateful for it.<break time="0.5s" /> And I am grateful for them.

Bradford Wheeler, M.P.H."""
    },
    "chapter_10_building_the_inevitable": {
        "title": "Chapter X — Building the Inevitable",
        "text": """Those studies established a baseline. But they also surfaced a limitation that would shape everything that followed. Syndromic surveillance does not cleanly surface the distinction between visits coded for a behavioral health diagnosis and visits coded with one. A person presenting with chest pain who also carries a depression diagnosis looks different in the data than one presenting in acute psychiatric crisis — but the coding alone may not tell you which is which. The studies had noted that behavioral health diagnoses concentrated increasingly with age, a pattern that did not fit the shape of the behavioral health emergency as experienced on the ground. Older patients accumulate diagnoses. That accumulation was inflating the picture.

There is a thus-unspoken hypothesis worth naming. The accumulation of behavioral health diagnosis codes with age may not reflect a true increase in acute behavioral need. It may instead reflect the normal operation of care engagement and screening processes deployed across health systems — systems operating with their own incentives. A patient who regularly sees a primary care physician accumulates diagnoses over time not necessarily because their condition is worsening, but because they are being seen, screened, and coded. The diagnosis code follows the encounter, not always the crisis. When those codes flow into surveillance data, they bring with them the fingerprint of care utilization rather than the signal of acute need. A system that rewards documentation, that ties reimbursement to diagnostic specificity, that prompts screening at every encounter, will produce data that looks like a behavioral health epidemic concentrated in older, more regularly engaged patients — whether or not that is what is actually happening in the emergency department at two in the morning.

Addressing this required moving closer to the moment of arrival. The patient's chief complaint — the words used to describe why they came in — carries information that diagnosis codes cannot. We had been working to identify acute behavioral encounters using that signal instead. But chief complaint data is free text, inconsistently entered, and resistant to structured analysis by design. Careful curation was required. The concepts — syndromic signal, diagnostic noise, chief complaint language, acute behavioral need — would need to be interwoven in a way that produced something cogent and actionable.

It is worth acknowledging that adjudicated coded data — the kind produced by medical billing and claims systems — does exist, and in principle contains more precise diagnostic information. But it lives in a different silo, serves different customers, and arrives with a lag of approximately one year. For a real-time surveillance solution, that lag is disqualifying. By the time adjudicated data reflects a trend, the trend has already moved. Syndromic surveillance is faster, broader, and more actionable — but only if its signal can be made precise enough to be meaningful. That is the problem the chief complaint work is designed to solve.

Large language models offer a genuine path forward. The curation work that once required painstaking manual review becomes tractable at scale when a model can be trained to recognize the language of acute behavioral need across its many expressions. This is not a solved problem. But it is a solvable one, and it is exactly the kind of work that NC DETECT's infrastructure makes worth attempting.

That precision matters because the underlying phenomenon it illuminates is not just a diagnostic noise problem. It is a boarding problem. These were people in crisis arriving at an ED, receiving a decision to admit, and then waiting. Sometimes for hours. Sometimes for days. Stranded in a care setting not designed to hold them, while the system upstream figures out where they can go. Chief complaint curation, made tractable at scale, is not the end of the problem — it is the lens that finally makes psychiatric boarding visible enough to act on.

It was a hard problem. It was also, in a specific technical sense, a surveillance problem. And it turned out I knew some of the partners.

The work centered on NC DETECT and a question about what it could see. A recent enhancement to the system had begun receiving Admission, Discharge, and Transfer (ADT) messages from hospital partners, providing discharge datetimes that made it possible, for the first time, to estimate length of stay from surveillance data alone. If that signal was reliable, it could serve as a directional boarding flag — not a clinical record, but an honest, documented, population-level indicator of a problem that had been difficult to measure consistently across the state.

I called the approach building the inevitable.<break time="0.75s" /> It is, I'll admit, a grandiose name for what is fundamentally unglamorous work. But the logic behind it is straightforward. Some things need to exist. The field has been circling them for years. The policy moment is arriving whether the infrastructure is ready or not. And someone has to be willing to build toward them persistently and transparently, in full view of the partners whose trust makes the work legitimate.

The model we developed uses ADT-derived discharge datetimes to flag ED encounters exceeding twenty-four hours — a conservative threshold chosen deliberately. It is higher than the clinical standard of four hours post-admission decision, and higher than the federal ECAT quality measure threshold of eight hours that will become mandatory reporting for hospitals in 2028. ECAT operates as an electronic Clinical Quality Measure — an eCQM — which works differently from other measure collection methodologies. Rather than relying on abstracted or manually reported data, eCQMs are calculated directly from structured data in the electronic health record at the point of care, then transmitted to CMS. This means the data infrastructure hospitals build for ECAT compliance is native to their clinical systems in a way that older reporting frameworks are not. That distinction matters for the validation work: the timestamp data elements ECAT requires are generated at the bedside, which is precisely the kind of ground-truth source the NC DETECT validation exercise needs to test against. That gap is not a flaw. It is an honest acknowledgment of what syndromic surveillance can and cannot do. The model is directionally correct. It is not a substitute for clinical judgment. It says so plainly, and that plainness is a trust-building posture with the clinical partners whose participation makes the validation possible.

Because there is a validation gate, and it is real. The timestamp comparison exercise — ADT-derived discharge times against clinical records — either shows directional alignment or it doesn't. If it doesn't, the model doesn't publish. Naming that clearly, in advance, to the partners who are being asked to contribute their data, is part of what makes the collaboration credible rather than extractive.

The first is the approaching ECAT mandate. The timestamp data elements it requires overlap directly with what the NC DETECT validation exercise examines — one analytical investment addressing two problems. That alignment is not accidental. It is the kind of confluence that makes otherwise difficult policy conversations easier to have.

The second pressure is the policy change the work is ultimately designed to support. ADT-derived discharge datetimes are the foundation of the boarding signal, but their use is currently under scrutiny precisely because discharge datetime reporting is not uniformly required or consistently implemented across North Carolina facilities. The validation exercise addresses data quality retrospectively. A change to reporting requirements — through statute, regulation, or an update to the NCHESS reporting specification — addresses it prospectively and statewide. That change cannot be driven by public health alone. It requires collective endorsement from hospital partners, routed through the North Carolina Healthcare Association as the body with standing to carry the request forward.

The framework for getting there runs through a directional surveillance partnership loop — signal, surface, contextualize, refine — and a longer policy arc that ends with a standardized statewide reporting requirement that resolves the scrutiny at its source. It involves the state's behavioral health policy division, the clinical informatics leadership of hospital partners, EHR vendors who will need to configure for ECAT compliance, and a governance committee whose approval is required before any of this publishes.

It is, in other words, exactly the kind of work that requires scaffolding. Stakeholder calls. Project management. Legal review. A RACI matrix — Responsible, Accountable, Consulted, Informed — that names who is accountable for what, so that the complexity doesn't collapse into ambiguity when the pressure arrives.

It is worth noting that this kind of work is not without precedent — and the precedent matters, because it establishes that legal authority for chief-complaint-driven intervention already exists in at least one well-documented case. In Cook County, Illinois, public health epidemiologists used emergency department syndromic surveillance data — chief complaint and discharge diagnosis fields — to identify substantial underreporting of potential rabies exposures and post-exposure prophylaxis. That finding did not stop at description. It triggered interventions to improve reporting compliance, under existing mandatory reporting authority for rabies exposure. The chain ran cleanly: syndromic signal, identified gap, intervention, improved data quality. If that chain can run for rabies, the architecture for it to run for behavioral health is not a legal novelty. The question is whether the specific authority extends this far — but the precedent for the shape of the work, from signal to intervention, is already established.

There is an unresolved question underneath all of this, and it deserves to be named rather than smoothed over. The legal authority for syndromic surveillance — the statutory and regulatory basis that allows a system like NC DETECT to exist and to be used the way it is used — was largely established more than two decades ago. That foundation has done real work. Researchers used near real-time morbidity data from the system to identify heat-related illness prevention strategies in North Carolina, and later evaluated and refined the state's heat syndrome case definition by analyzing emergency department visits across the system. This is the kind of work the authority was built for: a defined syndrome, a defined population, a defined public health response.

But that authority was written for a narrower set of use cases than the system has grown into. It did not anticipate behavioral health boarding as a syndromic surveillance application. It did not anticipate a world where chief complaint text might be processed by language models to identify acute psychiatric need. It did not anticipate the full system of practice that has since been built on top of it.

This is not a hypothetical concern. Whether the use we are now proposing falls cleanly within the authority that was granted, or sits in some grayer area that has simply not yet been tested, is a live question — one that does not yet have a clean answer. That uncertainty is not a reason to stop. But it is a reason to be honest about where the work currently stands. The technical pieces — the model, the validation gate, the policy loop — can all be built. Whether they can be deployed at scale may depend on a conversation about authority that has not yet happened, conducted by people whose job it is to have it.

That conversation is part of building the inevitable too. Infrastructure without authority is a blueprint. Authority without infrastructure is a permission nobody can use. Both have to arrive, and right now, only one of them is further along than the other.

This is the new ocean. The currents are unfamiliar. The partners are known. The destination is not yet visible, but the direction is clear. And the work is worth doing because the people waiting in those emergency departments are not abstractions. They are the same people this piece has been about from the beginning — people moving through systems that were not designed to hold them, showing up in data that was not designed to find them, waiting for an infrastructure that has not yet arrived.<break time="1.5s" />

We are building it."""
    },
    "chapter_9_into_new_waters": {
        "title": "Chapter IX — Into New Waters",
        "text": """To the colleagues I was closest to, I said it plainly: it was time to pursue a new opportunity rather than go back in the box. I'm not sure the metaphor landed the way I meant it. But I knew what I meant. The box was familiar. The box was safe. And the box was no longer where the work was.

What COVID had started in me wasn't finished. The response had cracked something open — a way of working across systems, of building under pressure, of seeing public health as something more elastic and interconnected than any single program could contain. I wanted to follow that. Not manage it from a familiar chair, but actually follow it somewhere new.

There was also something else I had to be honest with myself about. The work I was leaving deserved people who were arriving at it fresh — with energy I no longer had for it, with questions I had already asked, with the kind of generative uncertainty that makes a program grow. Staying too long in a role you've outgrown isn't loyalty. It's a slow way of taking up space that belongs to someone else. The system needed new talent. I needed to make room for it, and I needed to trust that it would come.

I want to be honest about the economics of it, because glossing over that would make this story tidier than it actually was. Stepping away from the data team meant leaving behind a small bonus, and the transition as structured wasn't attractive on its face. But when I learned about a need for a strategic data analyst role in the data office, a new topic area, a tough one, though with partners I already knew, it simply felt like the decision that made sense. An evolution of my analyst role into new waters.

The Data Office was not incidental to this story. They had housed the dashboard team — the people who had made the COVID response visible to the public, working in close proximity to external communications to ensure that what reached North Carolinians was accurate, timely, and legible. They had been part of the integration and governance discussions that I had watched from the data team side. And because of that, they had a vantage point that most of the organization didn't — a view across the landscape rather than from inside any single corner of it.

When I learned that the strategic data analyst role lived there, something clicked. These were people who already understood, at least in part, the argument I had been carrying. I wouldn't have to build the case from scratch. I could build from it.

The role itself was a genuinely new thing. A surveillance system data project in an applied area that hadn't been attempted before — no established methodology to inherit, no prior analyst to hand off from. The funding was time-limited, which meant the work carried its own quiet urgency. And I would soon find, as I settled into it, that I had not left the missing data problem behind. I had simply found a new version of it, in a new population, in a system that was just beginning to learn what it didn't know.

So the decision wasn't a departure. It was more like a hand-off — and a turn toward something I didn't yet fully understand.

I don't think the communicable disease framework is wrong. It's essential. But I had felt its edges — the places where the model stops and the harder, slower, less legible work begins. The work of upstream conditions. And I wasn't sure the program I was returning to had space for that tension, or appetite for what it implied.

So instead of stepping back through a familiar door, I chose to build something new.

The problem of behavioral health in the emergency department was not new to North Carolina's surveillance infrastructure. An early study using NC DETECT — North Carolina's statewide syndromic surveillance platform — described emergency department visits by patients with mental health diagnoses during 2008 through 2010, finding that nearly ten percent of ED visits carried a mental health diagnosis code, and that the rate of such visits grew seven times faster than the overall rate of ED visits during that period. A subsequent seven-year summary extended those findings through 2014, covering more than thirty-two million ED visits."""
    },
    "chapter_8_the_wind_down": {
        "title": "Chapter VIII — The Wind-Down",
        "text": """A simpler dashboard that provided the clearest summary metrics for a public with newer information, a more mature sense of community risk, and continued access to testing tools and vaccines through federal and state channels — at least for a time. COVID-19 vaccines transitioned to the commercial market in September 2023, ending the era of government-distributed doses that had defined the response. Free at-home COVID-19 tests through USPS were paused and restarted multiple times — including a pause beginning in March 2024 and at least a seventh distribution round launched in October 2024 — reflecting an ongoing, episodic rather than terminated, federal testing distribution effort. The infrastructure of the public health emergency was being quietly dismantled, piece by piece, even as the virus continued to circulate. The dashboards reflected that transition — not an ending, but a settling into something that looked more like endemic surveillance than emergency response.

This is what it looks like to build to the need, reassess the process, refactor for the future, and automate to minimize failure modes. The refactoring happened while the relay was still running. The automation was not a replacement for human judgment. It was a protection of it — freeing the team for the decisions that required interpretation, relationship, and context that no pipeline could supply.

The lesson underneath all of it was organizational, not technical. The code was the last thing written. The first things written were the roles, the relationships, the shared understanding of what the data meant and who it served. Scaling analytics is, at its core, a human problem. The machines follow.

When I announced I was leaving my role as data team lead — dropped into a branch-wide meeting without much ceremony — the response was a shower of virtual praise. Colleagues who had been through everything with me signaled, clearly and warmly, that they knew they were in good hands. There was no fear in the room. No apprehension. That mattered to me, because I remembered what it had felt like on the other side of that moment — when leadership had placed me into the role in the first place, during a wave of reassignment, attrition, and the joyous news of a colleague's maternity leave. That transition had been abrupt. This one would be planned.

The timeline stretched deliberately. There were successors to familiarize with the roles and duties, institutional knowledge to transfer, projects to hand off cleanly. By that point my work on the COVID data team looked less like leading and more like coaching — a co-coordinator for existing work rather than the engine driving it. That was, in its way, the lowest energy approach to an exit. The kind that leaves things better than you found them."""
    },
    "chapter_7_scaling_the_analytics": {
        "title": "Chapter VII — Scaling the Analytics",
        "text": """The earliest work was relational. Before there were dashboards or pipelines or automated outputs, there were people figuring out what the data meant, where it came from, and who needed to know what. Standing up analytics capacity in the middle of a public health emergency meant working with what was available — volunteers, temporary staff, CDC Foundation positions — and finding ways to build a functioning team out of a group that had not previously worked together, across time zones, under sustained pressure.

What emerged was a role-based model. Roles were documented, assigned, and revisited as the team evolved. Team culture had to be actively maintained. Human connectivity across time zones does not happen automatically; it has to be designed for, named, and tended. Microsoft Teams Shifts gave us a way to plan and coordinate across the relay. North Carolina had adopted Teams mere weeks before the state's first reported COVID case — which meant the platform arrived just as it was needed most, but without the organizational experience to use it to its full potential. Some groups had leaned into it early and built real working cultures around their channels — documents, threads, decision trails. Others ran on their own cadence, and their business documents lived in spaces disconnected from the broader infrastructure. The COVID analytics work was housed by the branch that owned most of the data and reporting work, but not all of the planning and communication lived there.

The channel was a partial picture of the work, not the whole of it. In practice, updated response summaries were communicated internally via email — a template that rarely changed and largely moved in one direction. The operational choreography fit the needs of the process. But the relay was fast and tightly dictated from the start, which had a natural consequence: it discouraged volunteers from getting in too deep. The process was reliable. It was also, by design, a little forbidding.

Another month of organizational experience before the pandemic arrived would likely have directed us toward a more intentional configuration — one that treated the channel as a genuine data hub, connected to the outputs the team was producing. The daily dashboard approval process might have been exactly the right place to test this. Think of it the way DevOps teams think about continuous integration and continuous improvement — a repeating, inspectable workflow where each cycle is an opportunity to catch problems early, tighten the handoff, and build confidence in the system. The dashboard relay had that shape already. With the right channel infrastructure behind it, it could have been a model for how the rest of the work was coordinated. We didn't have that month. But it is something worth trying again.

And it was a relay, with handoffs along the way. The daily process began at noon with a database snapshot of surveillance data, timed to coincide with the previous day's dashboard publication. A draft dashboard was made available for business review — a structured checkpoint in which the team verified the prior day's counts before authorizing deployment to the public.

From there, the handover to automated analytics required a trigger. A time-windowed CRON process began polling for a trigger file at a set time each day — choreographed to arrive when the surveillance extracts were expected to be complete. Think of it as a producer who shows up at the right moment, already knowing what the next scene requires, rather than waiting to be called. The alternative was an Outlook calendar notification, sent by the team lead to the dashboard analyst for the upcoming week, that someone would catch on a screen when it flashed. Those seconds mattered. They were critical business hours where quick action could mean the difference between a clean launch and a correction. If a launch failed, we could correct with a follow-up flight — or another if needed — and still make the noon deadline, accompanied by a simple status report. We were much more prepared for that contingency than we had been before.

What followed was a chained, scripted process: a sequential analytics workflow that ran on SAS, the analytics platform developed in Cary, North Carolina, whose licenses were heavily funded by the CDC. This step freed the team the equivalent of around forty hours of person-time per week — time that had largely translated to a download, run, upload cycle of number crunching to process and push datasets to network drives. By this point it was clear that a service account was needed to run all of these steps under a consistent identity, with consistent permissions, independent of any individual team member's machine or connection.

That last point mattered more than it might seem. The COVID data team had been able to engineer the core analytics processes as background or batch operations to a certain extent — but that approach was less resilient than it needed to be. Some teammates had faster machines. Others had slower internet speeds. The moment the analytics server spun up on the same local network as the surveillance system, those variables disappeared. The process stopped depending on whoever happened to be at their desk and started depending on infrastructure instead. That is a different kind of reliability — and a more honest one.

Sunday evenings included a weekly leadership report — a pre-built slide deck generated automatically, complete with graphics of the statewide epidemic curve broken down by the date bases that mattered. Date of symptom onset told the case narrative: when people actually got sick. Date of specimen collection reflected testing behavior and was the default picture for the public-facing dashboards. Date of report to the state system carried its own meaning, particularly for local partners — but it was not the same as the CDC's reporting date, which was calculated from statewide dashboard aggregate counts through a different methodology entirely.

Confused? Don't be. Some things are simply too squeaky when three separate levels of government are trying to agree on a single definition. Sometimes alignment is not achievable, and the honest response is to be clear about what each measure shows rather than pretending they are the same thing. Our dashboards were clear.

The automated Sunday slide deck was one of the proudest accomplishments of the team. It reduced the need for weekend work — a small but real act of stewardship toward the people who had been running the relay all week. The leads still checked in on Sunday logs, but the pre-built artifacts gave us the freedom to think about the Epidemiological Intelligence Briefing squarely within the work week, where it belonged.

The outputs from the analytics server moved to the testing team, who pivoted aggregate testing numbers and hybridized the two data sources for the dashboard counts. This reconciliation was necessary because the massive onboarding delay for electronic laboratory reporting had created multiple parallel reporting pathways that had to be tracked and managed simultaneously. A document called NoDuplicates tracked this work across the entirety of the response, a living record of the effort to make the counts coherent. Among the significant infrastructure built during this period, a lab reporting portal was established to summarize and track testing volume by laboratory identifier, bringing order to a landscape that had grown faster than any single system could absorb.

One of the more consequential additions to the pipeline was the capture of genotype data. The state had several pathways to receive this information from contracted laboratories — and notably, these tests arrived with explicit instructions that they were not clinical tests. That distinction mattered operationally and legally. But the data they carried was critical for decision-makers tracking the emergence and spread of variants. Getting it into the pipeline required building pipes between silos that had not previously been connected. The informatics team did that work thoughtfully, and the variant surveillance that followed — Delta, Omicron, and the decisions made in their wake — depended on it.

The Public Health Informatics Network team — the PHIN team — was essential for building reliable things, even when those things were made of squeaky parts. They distributed the operational load across communicable disease and lead surveillance work statewide — a scope that was real, adept, and genuinely adaptable, but not infinite. Their boundaries did not cross every public health program, and understanding where those boundaries fell was part of working with them effectively rather than around them.

One piece of that work was the lab archiving sharding logic. The surveillance system's person table needed to stay trimmed for the sake of performance — and at COVID volumes, that was not optional. Each week, batches of negative test records, which vastly outnumbered positives, were swept into cold storage and onto the analytics server. The operational system stayed fast for the people using it every day, while a complete record remained available for analytics. I had the chance to demonstrate the robustness of that sharding logic using file hashes — a proof simple enough to document cleanly and compelling enough to land. The confidence that demonstration established with leadership mattered: when I told them the details would be handled, they believed it.

Gary was the master of several ETL solutions that kept the operation running, and if he ever reads this, I owe him a few beers. But the system retired without achieving the full circular loop we had been working toward. The infrastructure went down with COVID — no other users, no other use cases had been stood up to employ it. That is a loss worth naming. The hardware had been tuned for the solution. The architecture was sound. The resources to achieve broader enterprise analytics automation were a single unicorn away from being solved. And remain so.

What closed the window was not failure but circumstance, arriving in layers. The data lead took a position in another division. Other diseases became priorities — Mpox brought its own demands for expertise, education, and public messaging that required the team's full attention. NCEDSS, the state's communicable disease surveillance system, entered a code freeze ahead of a large application upgrade and re-skin, which shut down the opportunity to upgrade the stack at the moment it might have mattered most. Eventually the operations team recomposed around new needs, and the window closed quietly rather than dramatically.

The infrastructure that had been built, tuned, and run at scale for two years did not find a second life. It is the kind of loss that does not make headlines — not a crash, not a cancellation, just a gradual dispersal of the people and conditions that had made something possible. What remains is the knowledge of what was built, and the confidence that it could be built again with the right long-term support behind it.

The code that orchestrated the daily batch process handled data cleaning, case and lab-level views for downstream analysis, reports, slide decks, and stakeholder outputs for NCHA, CDC, academic partners, and program leadership. It produced two logs that could be inspected in real time, making the most common failure modes visible before they became crises.

We went live with the scripted server processes on July 4, 2021. There is a certain grandiosity to that — and I will not pretend it was accidental. It was a holiday weekend, which made it on theme for the kind of work the team had been doing all along. The people who run a public health data operation don't stop because it's a weekend, or a holiday, or both. Going live on Independence Day felt like the right kind of symbolism for a process designed to give the team some of their time back. Like the file hash proof that confirmed not a single record had been lost, it didn't hurt to mark a moment of pride with a little ceremony."""
    },
    "chapter_4_paradigm_problem": {
        "title": "Chapter IV — The Paradigm Problem",
        "text": """The Paradigm Problem.

Mervyn Susser saw this coming.

Writing in the mid-1990s with his son Ezra, he argued that the dominant paradigm of his era — risk factor epidemiology — was growing less serviceable. It had done extraordinary work. The identification of individual-level risk factors had reshaped medicine and public health across the second half of the twentieth century. But the paradigm had a ceiling. By focusing relentlessly on proximate causes at the individual level, it left systematically understudied the forces acting at other levels — social, environmental, structural — that determined why some people were exposed to risk in the first place and others were not.

He called what he saw coming eco-epidemiology. The image he reached for was Chinese boxes — nested levels of organization, each containing the one below it, each requiring its own methods and its own questions. Molecular epidemiology at the innermost level. Individual risk factors in the middle. Social and environmental contexts at the outermost ring. The argument was not that risk factors didn't matter. It was that a single-level paradigm, however well executed, could not see the whole problem. The web of causation had a spider, and risk factor epidemiology wasn't looking for it.

What he described as an intellectual limitation of the paradigm, I kept recognizing as an institutional one. Applied public health had inherited a siloed structure from the disciplines that preceded it. Programs organized around disease categories. Data systems organized around programs. Funding organized around data systems. Each level optimized for its own outputs, accountable to its own metrics, largely incurious about what was happening one box out.

The result was a kind of enforced myopia. Not malicious — institutional myopia rarely is. But consequential. The Arant and Rosen study had made the court system's role in viral suppression visible in the data. But the data was only telling part of the story. I had seen another part of it through my time working with the state's AIDS Drug Assistance Program, known as HMAP. Jails across North Carolina had various arrangements in place to bridge medications for people entering custody. Some were thoughtful and well-coordinated. Others were not. The continuity of HIV medications — the thing that produces and sustains viral suppression — depended on arrangements that were locally negotiated, inconsistently implemented, and largely invisible to the surveillance system tracking the outcome.

There was something else I had learned, through Dr. Michelle Ogle — a clinician and former member of the Presidential Advisory Council on HIV/AIDS — about what sustaining suppression actually requires at the level of the body and the life. HIV medications need to be taken with food. Not as a preference, but as a clinical necessity — absorption, tolerability, adherence. Dr. Ogle's practice had recognized that prescribing the medication was not enough. They installed a food pantry. Not as a charitable gesture, but as a clinical intervention. Food is medicine. And medicine that is taken regularly, with adequate nutrition, produces viral suppression. Viral suppression is prevention. The dividend — the reduction in transmission, the sustained health of the patient, the cost avoided downstream — is real and measurable. But it only appears when the system is designed to maximize health outcomes rather than simply to deliver a prescription.

What the surveillance metric recorded was the outcome. What it could not see was the food pantry, the jail medication bridge, the broken appointment, the lapsed insurance. A communicable disease branch measuring suppression rates was measuring the shadow of a system it couldn't see. He would have recognized the problem immediately. The outcome lived at one level. The causes lived in the boxes surrounding it.

His prescription was integration — not the dissolution of levels, but the explicit recognition of their connections and a commitment to designing research and practice that could move between them. That is harder than it sounds in a system that funds silos, staffs silos, and measures the outputs of silos. The Chinese boxes are real. But the walls between them are largely institutional, not epidemiological. They reflect how we organized ourselves, not how disease actually moves through the world.

This was the tension I kept returning to. Not just in the data. In the very structure of how we organized ourselves to act."""
    }
}

CHAPTERS = {"chapter_2_the_infrastructure": CHAPTERS_ALL["chapter_2_the_infrastructure"]}

TEXT_SUBS = {
    "Susser's": "Süßer's",
    "Susser": "Süßer",
    "Arant": "Arrant",
    "HMAP": "eighchmap",
    "bivalent": "bivaylent",
    "U=U": "U equals U",
    "CSTE": "see ess tee ee",
    "SAS": "Sass",
    "NoDuplicates": "No Duplicates",
    "NCEDSS": "en see edds",
    "NCHA": "NC Healthcare Association",
    "PHIN": "fin",
    "ETL": "ee tee el",
    "USPS": "U S P S",
    "NC DETECT": "en see detect",
    "strategic data analyst": "strategic-data-analyst",
    "ECAT": "ee-cat",
    "eCQMs": "ee see queue ems",
    "eCQM": "ee see queue em",
    "CMS": "C.M.S.",
    "NCHESS": "en chess",
    "RACI": "ray-see",
    "brain bleed": "traumatic brain injury",
    "Hakenewerth": "Hackenworth",
    "EMTs": "E.M.T.s",
    "health holds": "health-holds",
    "DOT": "D.O.T.",
    "M.P.H.": "em pee aitch",
    "Researchers": "Reesurchers",
    "researchers": "reesurchers",
    "research": "reesearch",
    "Research": "Reesearch",
}

def prepare_text(text):
    for word, replacement in TEXT_SUBS.items():
        text = text.replace(word, replacement)
    if '<break' in text:
        text = f"<speak>{text}</speak>"
    return text

os.makedirs("audio", exist_ok=True)

for filename, chapter in CHAPTERS.items():
    print(f"Generating: {chapter['title']}...")
    response = requests.post(
        URL,
        json={
            "text": prepare_text(chapter["text"]),
            "model_id": "eleven_flash_v2",
            "voice_settings": VOICE_SETTINGS,
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
