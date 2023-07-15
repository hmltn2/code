const vscode = require('vscode');

function activate(context) {
    let disposable = vscode.commands.registerCommand('extension.helloWorld', function () {
        vscode.window.showInformationMessage('Hello, World!');
    });

    context.subscriptions.push(disposable);
}
exports.activate = activate;

