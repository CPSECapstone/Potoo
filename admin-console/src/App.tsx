import { BrowserRouter, Route, Link } from 'react-router-dom';
import AdminPanel from './admin-panel/AdminPanel';
import AgentPanel from './agent-panel/AgentPanel';

function AppRouter() {
   return (
     <BrowserRouter>
       <div>
            <nav>
               <ul>
               <li>
                 <Link to="/admin">Admin Panel</Link>
               </li>
               <li>
                 <Link to="/">Agent Panel</Link>
               </li>
             </ul>
           </nav>

           <Route path="/admin" exact component={AdminPanel} />
           <Route path="/" component={AgentPanel} />
         </div>
       </BrowserRouter>
     );
   }

 export default AppRouter;
