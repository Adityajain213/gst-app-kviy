from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import openpyxl
import os


class GSTLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.add_widget(Label(text="GST Number"))
        self.gst_input = TextInput(multiline=False)
        self.add_widget(self.gst_input)

        self.add_widget(Label(text="Company Name"))
        self.name_input = TextInput(multiline=False)
        self.add_widget(self.name_input)

        self.add_widget(Label(text="Amount"))
        self.amount_input = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.amount_input)

        self.add_button = Button(text="Add Data", size_hint_y=None, height=50)
        self.add_button.bind(on_press=self.add_data)
        self.add_widget(self.add_button)

        self.download_button = Button(text="Download File Info", size_hint_y=None, height=50)
        self.download_button.bind(on_press=self.show_file_path)
        self.add_widget(self.download_button)

        self.delete_button = Button(text="Delete File", size_hint_y=None, height=50)
        self.delete_button.bind(on_press=self.delete_file)
        self.add_widget(self.delete_button)

    def get_file_path(self):
        return os.path.join(App.get_running_app().user_data_dir, "GST_Data.xlsx")

    def add_data(self, instance):
        gst = self.gst_input.text
        name = self.name_input.text
        amount = self.amount_input.text

        if not gst or not name or not amount:
            self.show_popup("Please fill all fields")
            return

        filepath = self.get_file_path()

        if os.path.exists(filepath):
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
        else:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["GST Number", "Company Name", "Amount"])

        sheet.append([gst, name, amount])
        workbook.save(filepath)

        self.gst_input.text = ''
        self.name_input.text = ''
        self.amount_input.text = ''

        self.show_popup("Data Added Successfully")

    def show_file_path(self, instance):
        self.show_popup(f"Excel File Path:\n{self.get_file_path()}")

    def delete_file(self, instance):
        filepath = self.get_file_path()
        if os.path.exists(filepath):
            os.remove(filepath)
            self.show_popup("Excel File Deleted")
        else:
            self.show_popup("No file found to delete")

    def show_popup(self, message):
        popup = Popup(title="Info", content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()


class GSTApp(App):
    def build(self):
        return GSTLayout()


if __name__ == '__main__':
    GSTApp().run()
