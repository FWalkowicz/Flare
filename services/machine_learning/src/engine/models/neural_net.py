from .pluginSchematics import base, descriptors

activation_functions = [
    "ReLU", "Sigmoida", "Softmax", "Log Loss"
]


class PluggableModel(base.BaseModel):

    def dictionary_name(self):
        return "Sieć neuronowa"

    def create(self, hyperparameters):
        self.num_layers = hyperparameters['num_layers']
        self.num_neurons = hyperparameters['num_neurons']
        self.hidden_activation_function = hyperparameters['hidden_activation_function']
        self.out_activation_function = hyperparameters['out_activation_function']

    def save():
        pass

    def load():
        pass

    def describe_params(self):
        return {
            'num_neurons': descriptors.Int("Ilość neuronów na warstwę"),
            'num_layers': descriptors.Int("Ilość warstw"),
            'hidden_activation_function': descriptors.ChooseOne(
                "Funkcja aktywacji użyta między warstwami ukrytymi",
                activation_functions),
            'out_activation_function': descriptors.ChooseOne(
                "Funkcja aktywacji użyta w warstwie wyjściowej",
                activation_functions)
        }

    def describe_train_data(self):
        return {
            'inputs': descriptors.List(
                [descriptors.Int(f"Wartość wejściowa neuronu {i}" for i in range(1, self.num_neurons))]
            ),
            'outputs': descriptors.List(
                [descriptors.Int(f"Wartość wyjściowa neuronu {i}" for i in range(1, self.num_neurons))]
            )
        }

    def describe_inference_data(self):
        return {
            'inputs': descriptors.List(
                [descriptors.Int(f"Wartość wejściowa neuronu {i}" for i in range(1, self.num_neurons))]
            )
        }