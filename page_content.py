import pandas as pd
from openai import OpenAI

class PageContent:

    def __init__(self, town_list):
        self.town_list = town_list
        api_key = open("api_key/api", "r").read()
        self.client = OpenAI(api_key=api_key)

    def _gpt_response(self, town_name):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"Kannst du einen Text mit der gleichen Struktur, den gleichen Themen und ungefähr"
                            f" der gleichen Länge"
                            f" angepasst für {town_name} anstatt für Aachen verfassen? Bitte nutze Textabsätze nach"
                            f" Themen. "
                            f"Textreferenz: 'Aachen ist eine faszinierende Stadt im Westen Deutschlands mit einer "
                            f"Bevölkerung von etwa 250.000 Menschen."
                            f" Als historische Stadt mit einer reichen kulturellen Tradition ist Aachen bekannt für"
                            f" ihre beeindruckende Architektur,"
                            f" ihre renommierte Universität und ihre multikulturelle Atmosphäre. Die Stadt vereint "
                            f"Geschichte, Bildung und Lebensqualität auf eindrucksvolle Weise. "
                            f"Der Wohnungsbau in Aachen hat in den letzten Jahren eine dynamische Entwicklung erlebt."
                            f" Neue Wohnprojekte wurden realisiert, um dem steigenden Bedarf an Wohnraum gerecht "
                            f"zu werden."
                            f" Moderne Wohnanlagen, sorgfältig restaurierte Altbauten und zeitgemäße Neubauten bieten "
                            f"eine breite Palette an Wohnmöglichkeiten."
                            f" Besonders gefragt sind Wohnungen in zentralen Bezirken wie der Altstadt, dem "
                            f"Frankenberger Viertel und Burtscheid sowie in grünen Vororten."
                            f" Aachen ist auch ein bedeutendes Zentrum für Wissenschaft und Technologie."
                            f" Die Stadt beherbergt eine renommierte Technische Hochschule sowie zahlreiche "
                            f"Forschungsinstitute und Unternehmen"
                            f" aus verschiedenen Branchen wie Informationstechnologie, Biotechnologie und Maschinenbau. "
                            f"Aachen zeichnet sich durch ihre Innovationskraft,"
                            f" ihre wirtschaftliche Dynamik und ihre international ausgerichtete "
                            f"Forschungslandschaft aus. "
                            f" Die Mietpreise für Wohnungen in Aachen variieren je nach Lage und Ausstattung. "
                            f"Im Durchschnitt liegen die Mietkosten bei etwa 11 € pro Quadratmeter."
                            f" Trotzdem bleibt Aachen aufgrund ihrer historischen Bedeutung,"
                            f" ihrer kulturellen Vielfalt und ihrer hochwertigen Lebensqualität ein attraktiver "
                            f"Wohnort für Menschen aus aller Welt."
                            f" Aachen ist eine Stadt mit einer dynamischen Entwicklung."
                            f" Der Wohnungsbau, die wirtschaftliche Stärke und die kulturelle Vielfalt prägen das "
                            f"Stadtbild und tragen zum Wachstum bei."
                            f" Die Stadt bietet eine reiche Kulturszene, eine beeindruckende Architektur und eine "
                            f"hohe Lebensqualität."
                            f" In diesem dynamischen Umfeld sind moderne Vermarktungstechniken wie 3D-Visualisierungen "
                            f"ein wichtiger Faktor,"
                            f" um potenzielle Kunden zu überzeugen und den Erfolg von Bauunternehmen und "
                            f"Projektentwicklern zu fördern.'"}
            ]
        )
        definition = response.choices[0].message.content.strip("\n").strip()

        return definition

    def arch_vis_content(self):

        data = {"TITLE": [None], "TEXT1": [None], "TEXT2": [None], "TEXT3": [None], "TAGS": [None]
                }
        self.df = pd.DataFrame(data)

        for town_name in self.town_list:
            town_name_caps = town_name.upper()
            definition = self._gpt_response(town_name=town_name)
            new_row = {"TITLE": f"Architekturvisualisierung {town_name}",
                          "TEXT1": f"ARCHITEKTURVISUALISIERUNG IN DER REGION {town_name_caps}",
                          "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Visualisierung"
                                   f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                   f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                   f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                   f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                          "PROMPT": f"{definition}...",
                          "TAGS": f'["Architekturvisualisierung {town_name}", "Architektur", '
                                  f'"Visualisierung", "{town_name}"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

    def three_d_vis_content(self):

        data = {"TITLE": [None], "TEXT1": [None], "TEXT2": [None], "TEXT3": [None], "TAGS": [None]
                }
        self.df = pd.DataFrame(data)

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response(town_name=town_name)

            new_row = {"TITLE": f"3D Visualisierung {town_name}",
                          "TEXT1": f"3D VISUALISIERUNG IN DER REGION {town_name_caps}",
                          "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Visualisierung"
                                   f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                   f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                   f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                   f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                          "PROMPT": f"{definition}...",
                          "TAGS": f'["3D Visualisierung {town_name}", "3D-Visualisierung", "{town_name}"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

    def rendering_content(self):

        data = {"TITLE": [None], "TEXT1": [None], "TEXT2": [None], "TEXT3": [None], "TAGS": [None]
                }
        self.df = pd.DataFrame(data)

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response(town_name=town_name)

            new_row = {"TITLE": f"Rendering {town_name}",
                  "TEXT1": f"RENDERINGS IN DER REGION {town_name_caps}",
                  "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Renderings"
                           f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                           f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                           f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                           f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                  "PROMPT": f"{definition}..." ,
                  "TAGS": f'["Rendering {town_name}", "Rendering", "{town_name}", "3D"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

    def three_d_animation_content(self):

        data = {"TITLE": [None], "TEXT1": [None], "TEXT2": [None], "TEXT3": [None], "TAGS": [None]
                }
        self.df = pd.DataFrame(data)

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response(town_name=town_name)

            new_row = {"TITLE": f"3D Visualisierung {town_name}",
                       "TEXT1": f"3D VISUALISIERUNG IN DER REGION {town_name_caps}",
                       "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Visualisierung"
                                f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                       "PROMPT": f"{definition}...",
                       "TAGS": f'["3D Visualisierung {town_name}", "3D-Visualisierung", "{town_name}"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

    def immo_marketing_content(self):

        data = {"TITLE": [None], "TEXT1": [None], "TEXT2": [None], "TEXT3": [None], "TAGS": [None]
                }
        self.df = pd.DataFrame(data)

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response(town_name=town_name)

            new_row = {"TITLE": f"3D Visualisierung {town_name}",
                       "TEXT1": f"3D VISUALISIERUNG IN DER REGION {town_name_caps}",
                       "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Visualisierung"
                                f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                       "PROMPT": f"{definition}...",
                       "TAGS": f'["3D Visualisierung {town_name}", "3D-Visualisierung", "{town_name}"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

    def product_vis_content(self):

        data = {"TITLE": [None], "TEXT1": [None], "TEXT2": [None], "TEXT3": [None], "TAGS": [None]
                }
        self.df = pd.DataFrame(data)

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response(town_name=town_name)

            new_row = {"TITLE": f"3D Visualisierung {town_name}",
                       "TEXT1": f"3D VISUALISIERUNG IN DER REGION {town_name_caps}",
                       "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Visualisierung"
                                f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                       "PROMPT": f"{definition}...",
                       "TAGS": f'["3D Visualisierung {town_name}", "3D-Visualisierung", "{town_name}"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

    def vfx_content(self):

        data = {"TITLE": [None], "TEXT1": [None], "TEXT2": [None], "TEXT3": [None], "TAGS": [None]
                }
        self.df = pd.DataFrame(data)

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response(town_name=town_name)

            new_row = {"TITLE": f"3D Visualisierung {town_name}",
                       "TEXT1": f"3D VISUALISIERUNG IN DER REGION {town_name_caps}",
                       "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Visualisierung"
                                f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                       "PROMPT": f"{definition}...",
                       "TAGS": f'["3D Visualisierung {town_name}", "3D-Visualisierung", "{town_name}"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

    def three_d_modeling_content(self):

        data = {"TITLE": [None], "TEXT1": [None], "TEXT2": [None], "TEXT3": [None], "TAGS": [None]
                }
        self.df = pd.DataFrame(data)

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response(town_name=town_name)

            new_row = {"TITLE": f"3D Visualisierung {town_name}",
                       "TEXT1": f"3D VISUALISIERUNG IN DER REGION {town_name_caps}",
                       "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Visualisierung"
                                f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                       "PROMPT": f"{definition}...",
                       "TAGS": f'["3D Visualisierung {town_name}", "3D-Visualisierung", "{town_name}"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

    def export_csv(self, csv_name):
        self.df.to_csv("output/" + csv_name + ".csv", index=False)

