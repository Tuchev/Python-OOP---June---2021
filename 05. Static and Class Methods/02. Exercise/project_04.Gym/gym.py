class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer) -> bool:
        if customer in self.customers:
            return False
        self.customers.append(customer)

    def add_trainer(self, trainer) -> bool:
        if trainer in self.trainers:
            return False
        self.trainers.append(trainer)

    def add_equipment(self, equipment) -> bool:
        if equipment in self.equipment:
            return False
        self.equipment.append(equipment)

    def add_plan(self, plan) -> bool:
        if plan in self.plans:
            return False
        self.plans.append(plan)

    def add_subscription(self, subscription) -> bool:
        if subscription in self.subscriptions:
            return False
        self.subscriptions.append(subscription)

    @staticmethod
    def get_object(oid, cl_iterable):
        return list(filter(lambda _: _.id == oid, cl_iterable))[0]

    def subscription_info(self, subscription_id: int):
        csubscription = self.get_object(subscription_id, self.subscriptions)
        customer_id = csubscription.customer_id
        ccustomer = self.get_object(customer_id, self.customers)
        trainer_id = csubscription.trainer_id
        ctrainer = self.get_object(trainer_id, self.trainers)
        cplan = self.get_object(trainer_id, self.plans)
        cequipment = self.get_object(cplan.equipment_id, self.equipment)
        return f"{csubscription}\n{ccustomer}\n{ctrainer}\n{cequipment}\n{cplan}"
