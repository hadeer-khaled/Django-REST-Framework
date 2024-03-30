import { Outlet, createBrowserRouter } from "react-router-dom";
import Footer from "./components/Footer";
import Header from "./components/Header";
import Posts from "./components/Posts";
import PostLoading from "./components/PostLoading";

function Layout() {
  return (
    <>
      <Header />
      {/* Outlet component rendr any route [matches url pathname in browser] */}
      <Outlet />
      <Footer />
    </>
  );
}

const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Posts />,
      },
      {
        path: "/PostLoading",
        element: <PostLoading />,
      },
    ],
  },
]);

export default router;
