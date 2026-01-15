import streamlit as st
import pandas as pd
import random

# ---------------------------------------------------------
# 1. DATA PREPARATION
# ---------------------------------------------------------
# We stick to the B2 list we discussed.
# You can replace this with a CSV load if you prefer later.
# ---------------------------------------------------------
# EXPANDED B2 DATA SET
# ---------------------------------------------------------
data = [
    # --- AN (Akkusativ) ---
    {"verb": "denken", "prep": "an", "case": "Akkusativ", "trans": "to think of", "sentence": "Ich denke oft an meinen letzten Urlaub."},
    {"verb": "sich erinnern", "prep": "an", "case": "Akkusativ", "trans": "to remember", "sentence": "Erinnert ihr euch an den Namen des Lehrers?"},
    {"verb": "sich gewöhnen", "prep": "an", "case": "Akkusativ", "trans": "to get used to", "sentence": "Ich habe mich an das deutsche Wetter gewöhnt."},
    {"verb": "glauben", "prep": "an", "case": "Akkusativ", "trans": "to believe in", "sentence": "Glaubst du an Wunder?"},
    {"verb": "sich halten", "prep": "an", "case": "Akkusativ", "trans": "to stick to (rules)", "sentence": "Bitte halten Sie sich an die Regeln."},
    {"verb": "sich wenden", "prep": "an", "case": "Akkusativ", "trans": "to turn to (someone for help)", "sentence": "Bei Fragen wenden Sie sich bitte an den Support."},

    # --- AN (Dativ) ---
    {"verb": "arbeiten", "prep": "an", "case": "Dativ", "trans": "to work on", "sentence": "Wir arbeiten an einer Lösung für das Problem."},
    {"verb": "erkennen", "prep": "an", "case": "Dativ", "trans": "to recognize by", "sentence": "Ich habe ihn an seiner Stimme erkannt."},
    {"verb": "leiden", "prep": "an", "case": "Dativ", "trans": "to suffer from (disease)", "sentence": "Er leidet an einer schweren Grippe."},
    {"verb": "teilnehmen", "prep": "an", "case": "Dativ", "trans": "to participate in", "sentence": "Haben Sie an der Besprechung teilgenommen?"},
    {"verb": "zweifeln", "prep": "an", "case": "Dativ", "trans": "to doubt", "sentence": "Ich zweifle nicht an deiner Ehrlichkeit."},
    {"verb": "mangeln", "prep": "an", "case": "Dativ", "trans": "to lack", "sentence": "Es mangelt uns an qualifizierten Mitarbeitern."},

    # --- AUF (Akkusativ) ---
    {"verb": "achten", "prep": "auf", "case": "Akkusativ", "trans": "to pay attention to", "sentence": "Achten Sie bitte auf die Stufen!"},
    {"verb": "antworten", "prep": "auf", "case": "Akkusativ", "trans": "to answer", "sentence": "Er hat nicht auf meine E-Mail geantwortet."},
    {"verb": "aufpassen", "prep": "auf", "case": "Akkusativ", "trans": "to look after/watch", "sentence": "Kannst du kurz auf meine Tasche aufpassen?"},
    {"verb": "sich beziehen", "prep": "auf", "case": "Akkusativ", "trans": "to refer to", "sentence": "Ich beziehe mich auf Ihr Schreiben vom 12. Mai."},
    {"verb": "sich freuen (Zukunft)", "prep": "auf", "case": "Akkusativ", "trans": "to look forward to", "sentence": "Wir freuen uns auf die Zusammenarbeit."},
    {"verb": "hoffen", "prep": "auf", "case": "Akkusativ", "trans": "to hope for", "sentence": "Die Bauern hoffen auf Regen."},
    {"verb": "ankommen", "prep": "auf", "case": "Akkusativ", "trans": "to depend on (variable)", "sentence": "Es kommt auf das Wetter an, ob wir grillen."},
    {"verb": "sich konzentrieren", "prep": "auf", "case": "Akkusativ", "trans": "to concentrate on", "sentence": "Seid leise, ich muss mich auf den Text konzentrieren."},
    {"verb": "reagieren", "prep": "auf", "case": "Akkusativ", "trans": "to react to", "sentence": "Wie hat er auf die Nachricht reagiert?"},
    {"verb": "schimpfen", "prep": "auf", "case": "Akkusativ", "trans": "to rant about/scold", "sentence": "Alle schimpfen auf die hohen Benzinpreise."},
    {"verb": "sich verlassen", "prep": "auf", "case": "Akkusativ", "trans": "to rely on", "sentence": "Auf meine Freunde kann ich mich immer verlassen."},
    {"verb": "sich vorbereiten", "prep": "auf", "case": "Akkusativ", "trans": "to prepare for", "sentence": "Hast du dich gut auf die Prüfung vorbereitet?"},
    {"verb": "warten", "prep": "auf", "case": "Akkusativ", "trans": "to wait for", "sentence": "Ich warte auf den Bus."},
    {"verb": "verzichten", "prep": "auf", "case": "Akkusativ", "trans": "to do without", "sentence": "Ich kann nicht auf Schokolade verzichten."},

    # --- AUS (Dativ) ---
    {"verb": "bestehen", "prep": "aus", "case": "Dativ", "trans": "to consist of", "sentence": "Der Kurs besteht aus zwei Teilen."},
    {"verb": "schließen", "prep": "aus", "case": "Dativ", "trans": "to conclude from", "sentence": "Was schließen Sie aus diesem Verhalten?"},

    # --- FÜR (Akkusativ) ---
    {"verb": "danken", "prep": "für", "case": "Akkusativ", "trans": "to thank for", "sentence": "Ich danke Ihnen für Ihre schnelle Antwort."},
    {"verb": "sich entscheiden", "prep": "für", "case": "Akkusativ", "trans": "to decide in favor of", "sentence": "Er hat sich für das billigere Auto entschieden."},
    {"verb": "sich entschuldigen", "prep": "für", "case": "Akkusativ", "trans": "to apologize for", "sentence": "Ich möchte mich für die Verspätung entschuldigen."},
    {"verb": "halten", "prep": "für", "case": "Akkusativ", "trans": "to consider as", "sentence": "Ich halte das für eine gute Idee."},
    {"verb": "sich interessieren", "prep": "für", "case": "Akkusativ", "trans": "to be interested in", "sentence": "Interessierst du dich für Geschichte?"},
    {"verb": "kämpfen", "prep": "für", "case": "Akkusativ", "trans": "to fight for", "sentence": "Die Arbeiter kämpfen für höhere Löhne."},
    {"verb": "sorgen", "prep": "für", "case": "Akkusativ", "trans": "to ensure/take care of", "sentence": "Die Musik sorgte für gute Stimmung."},

    # --- GEGEN (Akkusativ) ---
    {"verb": "protestieren", "prep": "gegen", "case": "Akkusativ", "trans": "to protest against", "sentence": "Viele Menschen protestieren gegen das Gesetz."},
    {"verb": "sich wehren", "prep": "gegen", "case": "Akkusativ", "trans": "to defend oneself against", "sentence": "Du musst dich gegen diese Kritik wehren."},
    {"verb": "verstoßen", "prep": "gegen", "case": "Akkusativ", "trans": "to violate (law)", "sentence": "Das verstößt gegen die Regeln."},

    # --- IN (Akkusativ) ---
    {"verb": "geraten", "prep": "in", "case": "Akkusativ", "trans": "to get into (trouble/situation)", "sentence": "Er ist in Schwierigkeiten geraten."},
    {"verb": "sich verlieben", "prep": "in", "case": "Akkusativ", "trans": "to fall in love with", "sentence": "Sie hat sich in ihren Nachbarn verliebt."},

    # --- MIT (Dativ) ---
    {"verb": "anfangen", "prep": "mit", "case": "Dativ", "trans": "to start with", "sentence": "Wann fangen wir mit dem Essen an?"},
    {"verb": "aufhören", "prep": "mit", "case": "Dativ", "trans": "to stop doing something", "sentence": "Hör bitte mit dem Lärm auf!"},
    {"verb": "sich befassen", "prep": "mit", "case": "Dativ", "trans": "to deal with (topic)", "sentence": "Wir müssen uns mit diesem Thema befassen."},
    {"verb": "sich beschäftigen", "prep": "mit", "case": "Dativ", "trans": "to keep busy with", "sentence": "Er beschäftigt sich viel mit seinen Pflanzen."},
    {"verb": "rechnen", "prep": "mit", "case": "Dativ", "trans": "to expect/count on", "sentence": "Wir rechnen morgen mit Schnee."},
    {"verb": "sprechen (Partner)", "prep": "mit", "case": "Dativ", "trans": "to speak with", "sentence": "Kann ich kurz mit dir sprechen?"},
    {"verb": "streiten", "prep": "mit", "case": "Dativ", "trans": "to argue with", "sentence": "Ich möchte nicht mit dir streiten."},
    {"verb": "telefonieren", "prep": "mit", "case": "Dativ", "trans": "to talk on the phone with", "sentence": "Sie telefoniert gerade mit ihrer Mutter."},
    {"verb": "umgehen", "prep": "mit", "case": "Dativ", "trans": "to handle/deal with", "sentence": "Er kann gut mit Stress umgehen."},
    {"verb": "verbinden", "prep": "mit", "case": "Dativ", "trans": "to connect with", "sentence": "Können Sie mich mit Herrn Müller verbinden?"},
    {"verb": "vergleichen", "prep": "mit", "case": "Dativ", "trans": "to compare with", "sentence": "Man kann Äpfel nicht mit Birnen vergleichen."},
    {"verb": "zusammenhängen", "prep": "mit", "case": "Dativ", "trans": "to be related to", "sentence": "Das Problem hängt mit der Software zusammen."},
    {"verb": "zufrieden sein", "prep": "mit", "case": "Dativ", "trans": "to be satisfied with", "sentence": "Bist du mit deinem Gehalt zufrieden?"},

    # --- NACH (Dativ) ---
    {"verb": "fragen", "prep": "nach", "case": "Dativ", "trans": "to ask about", "sentence": "Ein Tourist fragte nach dem Weg."},
    {"verb": "sich erkundigen", "prep": "nach", "case": "Dativ", "trans": "to inquire about", "sentence": "Ich möchte mich nach den Preisen erkundigen."},
    {"verb": "riechen", "prep": "nach", "case": "Dativ", "trans": "to smell of", "sentence": "Hier riecht es nach frischem Kaffee."},
    {"verb": "schmecken", "prep": "nach", "case": "Dativ", "trans": "to taste like", "sentence": "Das Eis schmeckt nach Erdbeeren."},
    {"verb": "suchen", "prep": "nach", "case": "Dativ", "trans": "to search for", "sentence": "Wir suchen nach einer Lösung."},

    # --- ÜBER (Akkusativ) ---
    {"verb": "sich ärgern", "prep": "über", "case": "Akkusativ", "trans": "to get annoyed about", "sentence": "Ärgerst du dich über den Stau?"},
    {"verb": "sich aufregen", "prep": "über", "case": "Akkusativ", "trans": "to get upset about", "sentence": "Reg dich nicht über Kleinigkeiten auf."},
    {"verb": "berichten (Topic)", "prep": "über", "case": "Akkusativ", "trans": "to report on", "sentence": "Die Zeitung berichtet über den Unfall."},
    {"verb": "sich beschweren", "prep": "über", "case": "Akkusativ", "trans": "to complain about", "sentence": "Der Gast beschwerte sich über das Zimmer."},
    {"verb": "diskutieren", "prep": "über", "case": "Akkusativ", "trans": "to discuss (topic)", "sentence": "Sie diskutieren über Politik."},
    {"verb": "sich freuen (Gegenwart)", "prep": "über", "case": "Akkusativ", "trans": "to be happy about", "sentence": "Ich freue mich über deinen Besuch."},
    {"verb": "sich informieren", "prep": "über", "case": "Akkusativ", "trans": "to get info about", "sentence": "Man sollte sich vorher über die Kosten informieren."},
    {"verb": "lachen", "prep": "über", "case": "Akkusativ", "trans": "to laugh about", "sentence": "Wir haben viel über den Witz gelacht."},
    {"verb": "nachdenken", "prep": "über", "case": "Akkusativ", "trans": "to think about/reflect", "sentence": "Ich muss über dein Angebot nachdenken."},
    {"verb": "reden", "prep": "über", "case": "Akkusativ", "trans": "to talk about", "sentence": "Wir reden selten über unsere Gefühle."},
    {"verb": "staunen", "prep": "über", "case": "Akkusativ", "trans": "to be astonished at", "sentence": "Ich staune über dein Wissen."},
    {"verb": "sich wundern", "prep": "über", "case": "Akkusativ", "trans": "to be surprised at", "sentence": "Ich wundere mich über seine Pünktlichkeit."},

    # --- UM (Akkusativ) ---
    {"verb": "sich bewerben", "prep": "um", "case": "Akkusativ", "trans": "to apply for", "sentence": "Sie bewirbt sich um ein Stipendium."},
    {"verb": "bitten", "prep": "um", "case": "Akkusativ", "trans": "to ask for (request)", "sentence": "Darf ich dich um einen Gefallen bitten?"},
    {"verb": "es geht", "prep": "um", "case": "Akkusativ", "trans": "it is about", "sentence": "In diesem Text geht es um Umweltschutz."},
    {"verb": "sich kümmern", "prep": "um", "case": "Akkusativ", "trans": "to take care of", "sentence": "Wer kümmert sich um den Hund?"},
    {"verb": "sich sorgen", "prep": "um", "case": "Akkusativ", "trans": "to worry about", "sentence": "Ich sorge mich um seine Gesundheit."},

    # --- VON (Dativ) ---
    {"verb": "abhängen", "prep": "von", "case": "Dativ", "trans": "to depend on", "sentence": "Das hängt vom Preis ab."},
    {"verb": "sich erholen", "prep": "von", "case": "Dativ", "trans": "to recover from", "sentence": "Er muss sich noch von der Operation erholen."},
    {"verb": "erzählen", "prep": "von", "case": "Dativ", "trans": "to tell about", "sentence": "Erzähl mir von deiner Reise!"},
    {"verb": "halten", "prep": "von", "case": "Dativ", "trans": "to think of (opinion)", "sentence": "Was hältst du von meinem Vorschlag?"},
    {"verb": "handeln", "prep": "von", "case": "Dativ", "trans": "to be about (plot)", "sentence": "Der Film handelt von einem Musiker."},
    {"verb": "träumen", "prep": "von", "case": "Dativ", "trans": "to dream of", "sentence": "Ich träume von einem eigenen Haus."},
    {"verb": "unterscheiden", "prep": "von", "case": "Dativ", "trans": "to distinguish from", "sentence": "Er unterscheidet sich sehr von seinem Bruder."},
    {"verb": "überzeugen", "prep": "von", "case": "Dativ", "trans": "to convince of", "sentence": "Ich bin von seiner Unschuld überzeugt."},
    {"verb": "wissen", "prep": "von", "case": "Dativ", "trans": "to know about", "sentence": "Ich weiß nichts von diesem Plan."},

    # --- VOR (Dativ) ---
    {"verb": "Angst haben", "prep": "vor", "case": "Dativ", "trans": "to be afraid of", "sentence": "Viele Menschen haben Angst vor Spinnen."},
    {"verb": "schützen", "prep": "vor", "case": "Dativ", "trans": "to protect from", "sentence": "Die Creme schützt vor Sonnenbrand."},
    {"verb": "warnen", "prep": "vor", "case": "Dativ", "trans": "to warn against", "sentence": "Man hat uns vor dem Sturm gewarnt."},

    # --- ZU (Dativ) ---
    {"verb": "einladen", "prep": "zu", "case": "Dativ", "trans": "to invite to", "sentence": "Ich lade dich zu meinem Geburtstag ein."},
    {"verb": "gehören", "prep": "zu", "case": "Dativ", "trans": "to belong to (group)", "sentence": "Frankreich gehört zur EU."},
    {"verb": "gratulieren", "prep": "zu", "case": "Dativ", "trans": "to congratulate on", "sentence": "Ich gratuliere dir zum Erfolg."},
    {"verb": "passen", "prep": "zu", "case": "Dativ", "trans": "to fit/suit", "sentence": "Die Krawatte passt nicht zu dem Hemd."},
    {"verb": "zählen", "prep": "zu", "case": "Dativ", "trans": "to count among", "sentence": "Er zählt zu den besten Spielern der Welt."}
]

# ---------------------------------------------------------
# 2. SESSION STATE MANAGEMENT
# ---------------------------------------------------------
# This keeps track of which card we are looking at and if it is flipped
if 'card_index' not in st.session_state:
    st.session_state.card_index = 0
    st.session_state.flipped = False
    random.shuffle(data) # Shuffle once at startup
    st.session_state.deck = data

def next_card():
    # Move to next card and reset flip state
    st.session_state.card_index = (st.session_state.card_index + 1) % len(st.session_state.deck)
    st.session_state.flipped = False

def flip_card():
    st.session_state.flipped = not st.session_state.flipped

# ---------------------------------------------------------
# 3. UI LAYOUT & CSS
# ---------------------------------------------------------
st.set_page_config(page_title="B2 German Flashcards", page_icon="🇩🇪")

# Custom CSS to make it look like a real card
st.markdown("""
<style>
    .flashcard {
        background-color: #f9f9f9;
        border: 2px solid #ddd;
        border-radius: 15px;
        padding: 50px;
        text-align: center;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .verb-text {
        font-size: 40px;
        font-weight: bold;
        color: #333;
    }
    .prep-text {
        font-size: 30px;
        color: #d63031; /* Red for emphasis */
        font-weight: bold;
    }
    .case-badge {
        background-color: #0984e3;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 16px;
        margin-top: 10px;
        display: inline-block;
    }
    .sentence-box {
        margin-top: 20px;
        font-style: italic;
        color: #555;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🇩🇪 telc B2 Verb-Prepositions")
st.progress((st.session_state.card_index + 1) / len(st.session_state.deck))

# Get current card data
card = st.session_state.deck[st.session_state.card_index]

# ---------------------------------------------------------
# 4. CARD DISPLAY LOGIC
# ---------------------------------------------------------
# We use a container to hold the card content
card_container = st.container()

with card_container:
    if not st.session_state.flipped:
        # --- FRONT SIDE ---
        st.markdown(f"""
        <div class="flashcard">
            <div style="font-size: 20px; color: #888;">VERB</div>
            <div class="verb-text">{card['verb']}</div>
            <div style="font-size: 14px; color: #888; margin-top: 20px;">(Click Flip to reveal preposition)</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # --- BACK SIDE ---
        st.markdown(f"""
        <div class="flashcard">
            <div class="verb-text" style="font-size: 25px; margin-bottom: 10px;">{card['verb']}</div>
            <div class="prep-text">{card['prep']} <span style="color: #333;">+</span> <span class="case-badge">{card['case']}</span></div>
            <div style="margin-top: 10px; font-weight: bold;">{card['trans']}</div>
            <div class="sentence-box">"{card['sentence']}"</div>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. CONTROLS
# ---------------------------------------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🔄 FLIP CARD", use_container_width=True):
        flip_card()
        st.rerun()

    if st.button("➡️ NEXT CARD", use_container_width=True):
        next_card()
        st.rerun()

st.caption(f"Card {st.session_state.card_index + 1} of {len(st.session_state.deck)}")