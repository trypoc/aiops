import React, { Component } from "react";
import axios from "axios";
import "./App.css";
import PocContainer from "./client/PocContainer";

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      output: "",
      useCases: [],
      toolName: null
    };
  }

  getToolName = async () => {
    try {
      let res = await axios.get("http://localhost:4000/toolConfig.json");
      let { data } = res;
      console.log(`ToolName ${data.toolName}`);
      this.setState({ toolName: data.toolName });

      this.getUsecasesByToolName();
    } catch (error) {
      console.log("error in getToolName", error);
    }
  };

  getUsecasesByToolName = async () => {
    try {
      let res = await axios.get(
        "http://localhost:4000/" + this.state.toolName + "/usecase.json"
      );
      let { data } = res;
      this.setState({ useCases: data.usecases });
      console.log(`Usecases are  ${data.usecases}`);
    } catch (error) {
      console.log(`Error in getUsecasesByToolName ${error}`);
    }
  };

  componentDidMount() {
    this.getToolName();
  }

  render() {
    if (this.state.useCases.length > 0) {
      return (
        <PocContainer
          useCases={this.state.useCases}
          toolName={this.state.toolName}
        />
      );
    } else return null;
  }
}
