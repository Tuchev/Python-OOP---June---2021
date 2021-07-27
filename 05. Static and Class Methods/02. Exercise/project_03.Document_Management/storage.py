from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        cat = [c for c in self.categories if c.id == category_id][0]
        cat.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [topic for topic in self.topics if topic.id == topic_id]
        if topic:
            topic = topic[0]
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        doc = [d for d in self.documents if d.id == document_id][0]
        doc.edit(new_file_name)

    def delete_category(self, category_id):
        for cat in self.categories:
            if cat.id == category_id:
                self.categories.remove(cat)

    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                self.documents.remove(doc)

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return repr(doc)

    def __repr__(self):
        result = []
        for document in self.documents:
            result.append(repr(document))
        return "\n".join(result)
