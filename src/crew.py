from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
import os
from crewai.tools import tool

# Uncomment the following line to use an example of a custom tool
from src.tools.html_to_pdf_tool import HtmlToPdfTool
# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

@CrewBase
class CrewExperiment():
	"""CrewExperiment crew"""

	agents_config = "config/agents.yaml"
	tasks_config = "config/tasks.yaml"

	@before_kickoff # Optional hook to be executed before the crew starts
	def pull_data_example(self, inputs):
		# Example of pulling data from an external API, dynamically changing the inputs
		inputs['extra_data'] = "This is extra data"
		return inputs

	@after_kickoff # Optional hook to be executed after the crew has finished
	def log_results(self, output):
		# Example of logging results, dynamically changing the output
		print(f"Results: {output}")
		return output



	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[SerperDevTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	@agent
	def pdf_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['pdf_generator'],
			tools=[HtmlToPdfTool()],
			verbose=True
		)



	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.html'
		)


	@task
	def html_to_pdf_task(self) -> Task:
		return Task(
			config=self.tasks_config['html_to_pdf_task'],
			input_file='report.html',
			tools=[HtmlToPdfTool()],
			verbose=True
		)

	@crew
	def crew(self) -> Crew:

		"""Creates the CrewExperiment crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

