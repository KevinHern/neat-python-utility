from neat_exporter_package.neat_exporter.genome_to_json import discover_neural_network_layers
from neat_exporter_package.neat_exporter.models.connection import GenomeConnection
from random import randint

# Initializing dummy ID inputs
id_inputs = set()
id_inputs.add(-1)
id_inputs.add(-2)
id_inputs.add(-3)
id_inputs.add(-4)

# Initializing dummy ID outputs
id_outputs = set()
id_outputs.add(5)

# Initializing dummy connections
connections_keys = [
    (-1, 1), (-2, 2), (-3, 3), (-4, 4),
    (1, 6), (2, 6), (3, 7), (4, 7), (1, 8), (4, 8),
    (6, 9), (7, 9), (7, 10), (8, 10),
    (9, 5), (10, 5)
]

connections = list(
    map(lambda key: GenomeConnection(
            identification_number=key,
            enabled=True,
            weight=randint(0, 1024)
        ), connections_keys)
)

expected_layers = [
    {1, 2, 3, 4},
    {6, 7, 8},
    {9, 10},
    {5}
]

result = discover_neural_network_layers(
    id_inputs=id_inputs,
    id_outputs=id_outputs,
    connections=connections
)

print(result)

assert result == expected_layers
