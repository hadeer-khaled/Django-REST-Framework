import { Outlet, createBrowserRouter } from "react-router-dom";
import Footer from "./components/Footer";
import Header from "./components/Header";
import Post from "./components/Post";
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
        element: <Post />,
      },
      {
        path: "/PostLoading",
        element: <PostLoading />,
      },
    ],
  },
]);

export default router;
