import tkinter as tk
from es.es_service import EsService
import json


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=42, width=42)
        self.entry = tk.Entry(self)
        self.entry.focus()
        self.entry.pack()
        self.search_button = tk.Button(self, text="Search", command=lambda: self.search_text(self.entry.get()))
        self.search_button.pack()
        self.clear_button = tk.Button(self, text="Clear text", command=self.clear_text)
        self.clear_button.pack()

    def clear_text(self):
        self.entry.delete(0, 'end')

    def search_text(self, searchable_value: str):
        if searchable_value:
            es_service = EsService()
            data = json.loads(es_service.search(searchable_value).get().decode('utf-8'))['hits']['hits']
            self.set_data(data)
            self.entry.delete(0, 'end')

            return data

    def set_data(self, data: list):
        for item in data:
            print(item)

