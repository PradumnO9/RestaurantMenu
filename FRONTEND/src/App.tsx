import { useState } from "react";
function App() {
  const [count, setCount] = useState(0);

  return (
    <main className="py-10 bg-gray-50 h-screen">
      <h1 className="text-4xl font-bold">Hello Restaurant</h1>
    </main>
  );
}

export default App;
