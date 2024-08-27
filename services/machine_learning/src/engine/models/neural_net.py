from .pluggin_schematics import base, descriptors
import torch
import torch.nn as nn
import torch.optim as optim

activation_functions = ["ReLU", "Sigmoida", "Softmax", "Log Loss"]


class PluggableModel(base.BaseModel):

    def dictionary_name(self):
        return "Sieć neuronowa"

    def create(self, hyperparameters):
        self.num_layers = hyperparameters["num_layers"]
        self.num_neurons = hyperparameters["num_neurons"]
        self.hidden_activation_function = hyperparameters["hidden_activation_function"]
        self.out_activation_function = hyperparameters["out_activation_function"]

        activation_function_map = {
            "ReLU": nn.ReLU,
            "Sigmoid": nn.Sigmoid,
            "Softmax": lambda: nn.Softmax(dim=1),
            "LogSoftmax": lambda: nn.LogSoftmax(dim=1),
        }

        hidden_activation_func = activation_function_map[self.hidden_activation_function]()
        out_activation_func = activation_function_map[self.out_activation_function]()

        self.model = nn.Sequential()
        # Add hidden layers
        for i in range(self.num_layers):
            in_features = self.num_neurons if i > 0 else self.num_neurons
            self.model.add_module(f"fc{i + 1}", nn.Linear(100, 100))
            self.model.add_module(f"activation{i + 1}", hidden_activation_func)

        # Add output layer
        self.model.add_module("output", nn.Linear(100, 1))
        self.model.add_module("output_activation", out_activation_func)
        return self.model

    def save(self):
        torch.save(self.model.state_dict(), 'neural_net.pt')

    def load(self):
        torch.load('neural_net.pt')

    def describe_params(self):
        return {
            "num_neurons": descriptors.Int("Ilość neuronów na warstwę"),
            "num_layers": descriptors.Int("Ilość warstw"),
            "hidden_activation_function": descriptors.ChooseOne(
                "Funkcja aktywacji użyta między warstwami ukrytymi",
                activation_functions,
            ),
            "out_activation_function": descriptors.ChooseOne(
                "Funkcja aktywacji użyta w warstwie wyjściowej", activation_functions
            ),
        }

    def describe_train_data(self):
        return {
            "inputs": descriptors.List(
                [
                    descriptors.Int(
                        f"Wartość wejściowa neuronu {i}"
                        for i in range(1, self.num_neurons)
                    )
                ]
            ),
            "outputs": descriptors.List(
                [
                    descriptors.Int(
                        f"Wartość wyjściowa neuronu {i}"
                        for i in range(1, self.num_neurons)
                    )
                ]
            ),
        }

    def describe_inference_data(self):
        return {
            "inputs": descriptors.List(
                [
                    descriptors.Int(
                        f"Wartość wejściowa neuronu {i}"
                        for i in range(1, self.num_neurons)
                    )
                ]
            )
        }
