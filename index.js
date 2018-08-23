#!/usr/bin/env node

const inquirer = require("inquirer");
const chalk = require("chalk");
const figlet = require("figlet");
const shell = require("shelljs");


const init = () => {
    console.log(
        chalk.green(
            figlet.textSync("Sindhu CLI >>", {
                font: "Ghost",
                horizontalLayout: "default",
                verticalLayout: "default"
            })
        )
    );
}


const run = async () => {

    init();
    // show script introduction
    // ask questions
    // create the file
    // show success message
};

run();