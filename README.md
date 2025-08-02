# 🖼️ Auto Caption AI

Auto Caption AI is a multilingual image captioning app that generates natural language descriptions for uploaded images using deep learning. It leverages the BLIP (Bootstrapped Language-Image Pretraining) transformer model for caption generation, supports translation into 9+ languages, and allows users to listen to the captions using text-to-speech (TTS).

---

## 🚀 Features

- 🧠 Generates accurate image captions using the **Salesforce BLIP model**
- 🌐 Translates captions into **9+ languages** using **MarianMT**
- 🔊 Converts text captions into speech using **gTTS**
- 📷 Upload `.jpg`, `.jpeg`, or `.png` images
- ⚡ Interactive UI built with **Streamlit**

---

## 🛠️ Tech Stack

- Python 3.10+
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Salesforce BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base)
- [MarianMT](https://huggingface.co/Helsinki-NLP)
- gTTS (Google Text-to-Speech)
- Streamlit
- Torch
- PIL (Python Imaging Library)

---

## 📦 Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/auto-caption-ai.git
cd auto-caption-ai
pip install -r requirements.txt
streamlit run app1.py
```

## 🌐 Supported Languages

- English  
- Hindi  
- Tamil  
- Telugu  
- Bengali  
- Gujarati  
- French  
- Spanish  
- German  

---

## 🧪 How It Works

1. Upload an image (`.jpg`, `.jpeg`, or `.png`)
2. The BLIP model generates a caption in English
3. Select a target language to translate the caption (optional)
4. Translated caption is displayed
5. Click 🔊 **Listen to Caption** to hear it via text-to-speech

---

## 📷 Example

- **Image Input:** A person riding a motorcycle on a dirt road  
- **Generated Caption (English):** A man riding a motorcycle on a dirt road  
- **Translated (Spanish):** Un hombre montando una motocicleta en un camino de tierra  
- **Text-to-Speech:** 🔊 Audio plays caption aloud  

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Kirti Bohra**  
📧 [dhimankirti007@gmail.com](mailto:dhimankirti007@gmail.com)  
🔗 [GitHub](https://github.com/kirtiBohra12)  
🔗 [LinkedIn](https://www.linkedin.com/in/kirtibohra15)

---

## ⭐ Contributions

Feel free to fork the repo, suggest improvements, or raise issues. Contributions are always welcome!



pip install -r requirements.txt

