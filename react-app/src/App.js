import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import { authenticate } from "./store/session";
import { GetGames, PostGame, GetGame, DeleteGame, UpdateGame } from "./store/game"
import { getAllSkills, skills } from "./store/skills"
import { GetTeams, PostTeam, GetTeam, UpdateTeam, DeleteTeam } from "./store/team"
import { getGameJams, getGameJam, postGameJam, patchGameJam, deleteGameJam } from "./store/game_jam";



//***********
//Test imports
import SampleForm from "./components/chakra_lib/sample-form";
import StubPage from "./components/chakra_lib/stub-page";
import StubSteamMockup from "./components/chakra_lib/stub-steam-mockup";
import SampleNavBar from "./components/chakra_lib/navbar-sample";
import AnimatedGrid from "./components/chakra_lib/test-anime-grid"
import AnimatedGrid2 from "./components/chakra_lib/test-anime-grid2"
import FloatingCard from "./components/chakra_lib/floating-card";
import Podium from "./components/chakra_lib/podium";



function App() {
  const user = useSelector(state => state.session.user)
  const games = useSelector(state => state.session.games)
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());

      //Examples of api thinks

      // await dispatch(getTeam(1));
      // await dispatch(getTeams());
      await dispatch(getAllSkills());
      await dispatch(GetGames());

      // await dispatch(GetTeam(1));
      // await dispatch(GetTeams());
      // await dispatch(getAllSkills());
      // await dispatch(GetGames());


      // await dispatch(PostGame("testGame"))
      // await dispatch(GetGame(10))
      // await  dispatch(DeleteGame(12))
      // await  dispatch(UpdateGame(14, "MyTestUpdate"))

      await dispatch(getGameJams());

      setLoaded(true);
    })();
  }, []);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <SampleNavBar />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path="/users" exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute>
        <ProtectedRoute path="/" exact={true} >
          <h1>My Home Page</h1>
        </ProtectedRoute>





        {/*TEST ROUTES*/}
        <Route path="/sample-form" exact={true}>
          <SampleForm />
        </Route>
        <Route path="/stub-page" exact={true}>
          <StubPage />
        </Route>
        <Route path="/stub-steam-mockup" exact={true}>
          <StubSteamMockup />
        </Route>
        <Route path="/anime2">
            <AnimatedGrid2 />
        </Route>
        <Route path="/anime">
            <AnimatedGrid />
        </Route>
        <Route path="/carousel">
            <FloatingCard />
        </Route>
        <Route path="/winner-podium">
            <Podium />
        </Route>


        {/*HANDLE ERRORS*/}
        <Route path="/">
          Error 404
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
