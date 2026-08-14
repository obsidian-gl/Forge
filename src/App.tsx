/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

export default function App() {
  return (
    <div className="min-h-screen bg-neutral-950 text-neutral-200 flex flex-col items-center justify-center p-8 font-mono">
      <div className="max-w-2xl w-full space-y-6">
        <div className="text-center space-y-4">
          <h1 className="text-4xl font-bold text-cyan-400">⚡ FORGE</h1>
          <p className="text-xl text-neutral-400">Terminal Swiss Army Knife</p>
        </div>
        
        <div className="bg-neutral-900 border border-neutral-800 rounded-lg p-6 space-y-4">
          <p className="text-lg">
            This application is a <strong>Command Line Interface (CLI)</strong> tool.
          </p>
          <p className="text-neutral-400">
            To use it, please export or download this project, then run it in your local terminal:
          </p>
          
          <div className="bg-black border border-neutral-800 rounded p-4 overflow-x-auto">
            <pre className="text-green-400">
              <code>
{`# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the script
python forge.py`}
              </code>
            </pre>
          </div>
        </div>
      </div>
    </div>
  );
}
