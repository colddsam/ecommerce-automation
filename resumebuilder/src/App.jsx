import './App.css';
import NavBar from './Navbar/NavBar';
import Routers from './Router/Router';

export default function App() {
  return (
    <div className="h-screen w-screen bg-back-white flex flex-col justify-center items-start font-bold">
      <NavBar />
      <Routers />
    </div>
  )
}
