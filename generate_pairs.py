import csv
import json

PROMPT_END_SEPARATOR = " \n\n###\n\n"
COMPLETION_END_SEPARATOR = " END"

# Read CSV file
with open('data.csv', 'r') as file:
    raw_data = list(csv.reader(file, delimiter=','))
    headers = [header.strip() for header in raw_data[0]]  # Stripping whitespaces
    data = raw_data[1:]

# Create prompt and completion pairs
pairs = []
for sensor in data:
    # Skip rows with insufficient data
    if len(sensor) < len(headers):
        continue
    
    # Try constructing the prompt and completion
    try:
        prompt = f"Please provide a summary of the specifications for {sensor[headers.index('Sensor')]}."
        completion = f"{sensor[headers.index('Sensor')]} specifications include a supply voltage of {sensor[headers.index('Supply Voltage')]}, output types like {sensor[headers.index('Output')]}, accuracy of {sensor[headers.index('Accuracy')]}, repeatability at {sensor[headers.index('Repeatability')]}, resolution set to {sensor[headers.index('Resolution')]}, electrical angle or stroke parameters of {sensor[headers.index('Electrical Angle or Stroke')]}, and an operating temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"What is the supply voltage requirement for {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} requires a supply voltage of {sensor[headers.index('Supply Voltage')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"Can you tell me the necessary supply voltage for {sensor[headers.index('Sensor')]}?"
        completion = f"The necessary supply voltage for {sensor[headers.index('Sensor')]} is {sensor[headers.index('Supply Voltage')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"What output options are available for {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} has the following output options: {sensor[headers.index('Output')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"Can you specify the accuracy of the measurements for {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} provides measurements with an accuracy of {sensor[headers.index('Accuracy')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"How repeatable are the readings from {sensor[headers.index('Sensor')]}?"
        completion = f"The readings from {sensor[headers.index('Sensor')]} have a repeatability of {sensor[headers.index('Repeatability')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"What is the resolution of {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} has a resolution of {sensor[headers.index('Resolution')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"What is the electrical angle or stroke for {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} has an electrical angle or stroke of {sensor[headers.index('Electrical Angle or Stroke')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"What operating temperatures are supported by {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} can operate within a temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"Can you tell me about the resolution capabilities of {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} is capable of a resolution of {sensor[headers.index('Resolution')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"How accurate are the measurements taken by {sensor[headers.index('Sensor')]}?"
        completion = f"The measurements taken by {sensor[headers.index('Sensor')]} have an accuracy of {sensor[headers.index('Accuracy')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"What kind of electrical angle or stroke is supported by {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} supports an electrical angle or stroke of {sensor[headers.index('Electrical Angle or Stroke')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"At what temperature range can {sensor[headers.index('Sensor')]} operate effectively?"
        completion = f"{sensor[headers.index('Sensor')]} can effectively operate at a temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"What is the range of supply voltages compatible with {sensor[headers.index('Sensor')]}?"
        completion = f"The range of supply voltages compatible with {sensor[headers.index('Sensor')]} is {sensor[headers.index('Supply Voltage')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"How consistent are the readings taken by {sensor[headers.index('Sensor')]}?"
        completion = f"The readings taken by {sensor[headers.index('Sensor')]} are consistent with a repeatability of {sensor[headers.index('Repeatability')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"What kind of output signals can I expect from {sensor[headers.index('Sensor')]}?"
        completion = f"You can expect {sensor[headers.index('Sensor')]} to have output options of {sensor[headers.index('Output')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})

        prompt = f"What is the electrical angle or stroke measurement for {sensor[headers.index('Sensor')]}?"
        completion = f"The electrical angle or stroke measurement for {sensor[headers.index('Sensor')]} is {sensor[headers.index('Electrical Angle or Stroke')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What are the acceptable operating temperatures for {sensor[headers.index('Sensor')]}?"
        completion = f"The acceptable operating temperatures for {sensor[headers.index('Sensor')]} are {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What voltage should I use to power {sensor[headers.index('Sensor')]}?"
        completion = f"You should use a supply voltage of {sensor[headers.index('Supply Voltage')]} to power {sensor[headers.index('Sensor')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What types of signals does {sensor[headers.index('Sensor')]} output?"
        completion = f"{sensor[headers.index('Sensor')]} outputs the following types of signals: {sensor[headers.index('Output')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Is the data from {sensor[headers.index('Sensor')]} highly accurate?"
        completion = f"Yes, the data from {sensor[headers.index('Sensor')]} is highly accurate with an accuracy of {sensor[headers.index('Accuracy')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"How fine is the detail in the readings from {sensor[headers.index('Sensor')]}?"
        completion = f"The readings from {sensor[headers.index('Sensor')]} have a fine detail with a resolution of {sensor[headers.index('Resolution')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What are the specifications for the electrical angle or stroke of {sensor[headers.index('Sensor')]}?"
        completion = f"The specifications for the electrical angle or stroke of {sensor[headers.index('Sensor')]} are {sensor[headers.index('Electrical Angle or Stroke')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"In what temperature conditions can {sensor[headers.index('Sensor')]} be reliably used?"
        completion = f"{sensor[headers.index('Sensor')]} can be reliably used in temperature conditions ranging from {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What's the voltage input that {sensor[headers.index('Sensor')]} operates on?"
        completion = f"{sensor[headers.index('Sensor')]} operates on a voltage input of {sensor[headers.index('Supply Voltage')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Which output formats are supported by {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} supports the following output formats: {sensor[headers.index('Output')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Can you inform me about the measurement accuracy of {sensor[headers.index('Sensor')]}?"
        completion = f"The measurement accuracy of {sensor[headers.index('Sensor')]} is {sensor[headers.index('Accuracy')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What is the repeatability specification for {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} has a repeatability specification of {sensor[headers.index('Repeatability')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What's the finest detail that {sensor[headers.index('Sensor')]} can measure?"
        completion = f"{sensor[headers.index('Sensor')]} can measure details as fine as {sensor[headers.index('Resolution')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Could you tell me about the electrical angle or stroke parameters of {sensor[headers.index('Sensor')]}?"
        completion = f"The electrical angle or stroke parameters of {sensor[headers.index('Sensor')]} are {sensor[headers.index('Electrical Angle or Stroke')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What temperature ranges can {sensor[headers.index('Sensor')]} withstand during operation?"
        completion = f"{sensor[headers.index('Sensor')]} can withstand temperature ranges of {sensor[headers.index('Operating Temperature')]} during operation."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"How much voltage is needed for {sensor[headers.index('Sensor')]} to function properly?"
        completion = f"{sensor[headers.index('Sensor')]} requires {sensor[headers.index('Supply Voltage')]} to function properly."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What are the output signal types of {sensor[headers.index('Sensor')]}?"
        completion = f"The output signal types of {sensor[headers.index('Sensor')]} are {sensor[headers.index('Output')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"How reliable are the measurements taken by {sensor[headers.index('Sensor')]} in terms of accuracy?"
        completion = f"The measurements taken by {sensor[headers.index('Sensor')]} are reliable with an accuracy of {sensor[headers.index('Accuracy')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"How often can {sensor[headers.index('Sensor')]} produce consistent readings?"
        completion = f"{sensor[headers.index('Sensor')]} can produce consistent readings with a repeatability of {sensor[headers.index('Repeatability')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Can {sensor[headers.index('Sensor')]} discern very fine changes in measurements?"
        completion = f"Yes, {sensor[headers.index('Sensor')]} can discern very fine changes with a resolution of {sensor[headers.index('Resolution')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Could you give me a rundown of the key specifications for {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} has a supply voltage of {sensor[headers.index('Supply Voltage')]}, output options that include {sensor[headers.index('Output')]}, accuracy rated at {sensor[headers.index('Accuracy')]}, repeatability of {sensor[headers.index('Repeatability')]}, resolution of {sensor[headers.index('Resolution')]}, electrical angle or stroke parameters being {sensor[headers.index('Electrical Angle or Stroke')]}, and it operates within a temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Can you summarize the essential specifications of {sensor[headers.index('Sensor')]} for me?"
        completion = f"Certainly! The {sensor[headers.index('Sensor')]} operates at a supply voltage of {sensor[headers.index('Supply Voltage')]} and offers various output types including {sensor[headers.index('Output')]}. It has an accuracy of {sensor[headers.index('Accuracy')]} and features a repeatability of {sensor[headers.index('Repeatability')]} with a resolution of {sensor[headers.index('Resolution')]}. Furthermore, it measures electrical angle or stroke within parameters of {sensor[headers.index('Electrical Angle or Stroke')]} and is functional within an operating temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Can I get a brief overview of the specifications for {sensor[headers.index('Sensor')]}?"
        completion = f"Of course! {sensor[headers.index('Sensor')]} operates with a supply voltage of {sensor[headers.index('Supply Voltage')]} and offers output options such as {sensor[headers.index('Output')]}. It boasts an accuracy of {sensor[headers.index('Accuracy')]}, a repeatability of {sensor[headers.index('Repeatability')]}, and a resolution of {sensor[headers.index('Resolution')]}. The electrical angle or stroke is specified at {sensor[headers.index('Electrical Angle or Stroke')]}, and it’s capable of operating within a temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Please provide a summary of the specifications for {sensor[headers.index('Sensor')]}."
        completion = f"{sensor[headers.index('Sensor')]} specifications include a supply voltage of {sensor[headers.index('Supply Voltage')]}, output types like {sensor[headers.index('Output')]}, accuracy of {sensor[headers.index('Accuracy')]}, repeatability at {sensor[headers.index('Repeatability')]}, resolution set to {sensor[headers.index('Resolution')]}, electrical angle or stroke parameters of {sensor[headers.index('Electrical Angle or Stroke')]}, and an operating temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        promt = f"Can you compile the main features of {sensor[headers.index('Sensor')]} into a summary?"
        completion = f"Certainly, {sensor[headers.index('Sensor')]} has a variety of features including a supply voltage of {sensor[headers.index('Supply Voltage')]}, outputs such as {sensor[headers.index('Output')]}, an accuracy specification of {sensor[headers.index('Accuracy')]}, repeatability figures at {sensor[headers.index('Repeatability')]}, resolution capabilities of {sensor[headers.index('Resolution')]}, electrical angle or stroke within {sensor[headers.index('Electrical Angle or Stroke')]}, and an operational temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What is the specification of the electrical angle or stroke of {sensor[headers.index('Sensor')]}?"
        completion = f"The specification of the electrical angle or stroke of {sensor[headers.index('Sensor')]} is {sensor[headers.index('Electrical Angle or Stroke')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"At what range of temperatures is {sensor[headers.index('Sensor')]} designed to operate?"
        completion = f"{sensor[headers.index('Sensor')]} is designed to operate at a temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What are the electrical requirements for running {sensor[headers.index('Sensor')]}?"
        completion = f"The electrical requirements for running {sensor[headers.index('Sensor')]} include a supply voltage of {sensor[headers.index('Supply Voltage')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Can you elaborate on the types of outputs provided by {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} provides outputs in the form of {sensor[headers.index('Output')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"How certain can I be of the readings from {sensor[headers.index('Sensor')]}?"
        completion = f"You can be certain of the readings from {sensor[headers.index('Sensor')]} to an accuracy of {sensor[headers.index('Accuracy')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Is {sensor[headers.index('Sensor')]} capable of delivering consistent readings over time?"
        completion= f"Yes, {sensor[headers.index('Sensor')]} is capable of delivering consistent readings with a repeatability of {sensor[headers.index('Repeatability')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What's the granularity of measurements provided by {sensor[headers.index('Sensor')]}?"
        completion = f"The granularity of measurements provided by {sensor[headers.index('Sensor')]} is {sensor[headers.index('Resolution')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"In what range of environmental temperatures is {sensor[headers.index('Sensor')]} functional?"
        completion = f"{sensor[headers.index('Sensor')]} is functional in an environmental temperature range of {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What power need for {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} need power of {sensor[headers.index('Supply Voltage')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What type outputs {sensor[headers.index('Sensor')]} give?"
        completion = f"{sensor[headers.index('Sensor')]} give outputs like {sensor[headers.index('Output')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"How sure measurements of {sensor[headers.index('Sensor')]}?"
        completion = f"Measurements of {sensor[headers.index('Sensor')]} have accuracy {sensor[headers.index('Accuracy')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"{sensor[headers.index('Sensor')]} same results how many times?"
        completion = f"{sensor[headers.index('Sensor')]} give same results with repeatability {sensor[headers.index('Repeatability')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Details how small see {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} see details small like {sensor[headers.index('Resolution')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What electrical angle or stroke {sensor[headers.index('Sensor')]} measure?"
        completion = f"{sensor[headers.index('Sensor')]} measure electrical angle or stroke {sensor[headers.index('Electrical Angle or Stroke')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What temperatures {sensor[headers.index('Sensor')]} work in?"
        completion = f"{sensor[headers.index('Sensor')]} work in temperatures {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Voltage for {sensor[headers.index('Sensor')]} what is?"
        completion = f"Voltage for {sensor[headers.index('Sensor')]} is {sensor[headers.index('Supply Voltage')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Outputs what types {sensor[headers.index('Sensor')]}?"
        completion = f"{sensor[headers.index('Sensor')]} outputs types {sensor[headers.index('Output')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Measurements good how much {sensor[headers.index('Sensor')]}?"
        completion = f"Measurements good {sensor[headers.index('Accuracy')]} in {sensor[headers.index('Sensor')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"How steady readings {sensor[headers.index('Sensor')]} give?"
        completion = f"{sensor[headers.index('Sensor')]} give readings steady {sensor[headers.index('Repeatability')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"How fine details {sensor[headers.index('Sensor')]} catch?"
        completion = f"{sensor[headers.index('Sensor')]} catch fine details {sensor[headers.index('Resolution')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"Electrical angle or stroke for {sensor[headers.index('Sensor')]} what specs?"
        completion = f"Electrical angle or stroke for {sensor[headers.index('Sensor')]} have specs {sensor[headers.index('Electrical Angle or Stroke')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
        prompt = f"What temperature range {sensor[headers.index('Sensor')]} use in?"
        completion = f"{sensor[headers.index('Sensor')]} use in temperature range {sensor[headers.index('Operating Temperature')]}."
        pairs.append({"prompt": prompt + PROMPT_END_SEPARATOR, "completion": completion + COMPLETION_END_SEPARATOR})
        
    except ValueError as e:
        print(f"Error occurred: {e}. Current sensor data: {sensor}")
        continue


with open('prompt_completion_pairs.jsonl', 'w') as f:
    for pair in pairs:
        # Write each pair as a JSON-formatted string followed by a newline
        f.write(json.dumps(pair) + '\n')

