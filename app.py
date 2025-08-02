import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
import tempfile

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

# Language mappings
LANGUAGES = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Spanish": "es",
    "Tamil": "ta",
    "Bengali": "bn",
    "Telugu": "te",
    "Gujarati": "gu"
}

# Load translation model
@st.cache_resource
def load_translation_model(lang_code):
    model_name = f"Helsinki-NLP/opus-mt-en-{lang_code}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    translator = MarianMTModel.from_pretrained(model_name)
    return tokenizer, translator

# Translate captions
def translate_caption(text, target_lang_code):
    tokenizer, translator = load_translation_model(target_lang_code)
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = translator.generate(**inputs)
    tgt = tokenizer.decode(translated[0], skip_special_tokens=True)
    return tgt

# Generate captions
def predict_step(image_paths):
    captions = []
    for image_path in image_paths:
        image = Image.open(image_path)
        if image.mode != "RGB":
            image = image.convert("RGB")

        inputs = processor(images=image, return_tensors="pt").to(device)
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        captions.append(caption.strip())
    return captions

# Streamlit UI
st.set_page_config(page_title="Auto Caption AI", layout="centered")
st.title("🌍🖼️ Auto Caption AI")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
language = st.selectbox("Choose output language", list(LANGUAGES.keys()))

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    if image.mode != "RGB":
        image = image.convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Generating caption..."):
        caption_en = predict_step([uploaded_file])[0]

        if LANGUAGES[language] == "en":
            final_caption = caption_en
        else:
            final_caption = translate_caption(caption_en, LANGUAGES[language])

        st.success("Generated Caption:")
        st.write(f"📜 **{final_caption}**")

    # Text-to-Speech
    gtts_lang_map = {
        "en": "en", "fr": "fr", "de": "de", "hi": "hi", "es": "es",
        "ta": "ta", "bn": "bn", "te": "te", "gu": "gu"
    }

    if st.button("🔊 Listen to Caption"):
        lang_code = gtts_lang_map[LANGUAGES[language]]
        tts = gTTS(text=final_caption, lang=lang_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            tts.save(tmpfile.name)
            audio_file = open(tmpfile.name, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
