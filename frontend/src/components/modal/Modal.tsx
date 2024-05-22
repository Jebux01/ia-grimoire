import { forwardRef } from "react";
import clsx from "clsx";
import { styled, css } from "@mui/system";
import { Modal as BaseModal } from "@mui/base/Modal";

interface ModalUnstyledProps {
  open: boolean;
  onClose: () => void;
}

export default function ModalUnstyled({ open, onClose }: ModalUnstyledProps) {
  return (
    <div>
      <Modal
        aria-labelledby="unstyled-modal-title"
        aria-describedby="unstyled-modal-description"
        open={open}
        onClose={onClose}
        slots={{ backdrop: StyledBackdrop }}
      >
        <ModalContent sx={{ width: 400 }}>
          <h2 id="unstyled-modal-title" className="modal-title">
            Felicidades! 🎉 Has sido aceptado en la escuela de Magia
          </h2>
          <p id="unstyled-modal-description" className="modal-description">
            Ahora podrás aprender a lanzar hechizos y pociones mágicas. p.d esta
            prueba tecnica fue basada en el anime de Black Clover, se intento
            seguir algunos estilos del anime y easter eggs.
          </p>
          <p>
            <img
              src="https://i.pinimg.com/originals/61/52/ef/6152efd446827819d69818f9a612a9af.jpg"
              alt="Black Clover"
              width="100%"
              height="50%"
            />
          </p>
        </ModalContent>
      </Modal>
    </div>
  );
}

const Backdrop = forwardRef<
  HTMLDivElement,
  { open?: boolean; className: string }
>((props, ref) => {
  const { open, className, ...other } = props;
  return (
    <div
      className={clsx({ "base-Backdrop-open": open }, className)}
      ref={ref}
      {...other}
    />
  );
});

const grey = {
  50: "#F3F6F9",
  100: "#E5EAF2",
  200: "#DAE2ED",
  300: "#C7D0DD",
  400: "#B0B8C4",
  500: "#9DA8B7",
  600: "#6B7A90",
  700: "#434D5B",
  800: "#303740",
  900: "#1C2025",
};

const Modal = styled(BaseModal)`
  position: fixed;
  z-index: 1300;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const StyledBackdrop = styled(Backdrop)`
  z-index: -1;
  position: fixed;
  inset: 0;
  background-color: rgb(0 0 0 / 0.5);
  -webkit-tap-highlight-color: transparent;
`;

const ModalContent = styled("div")(
  ({ theme }) => css`
    font-family: "IBM Plex Sans", sans-serif;
    font-weight: 500;
    text-align: start;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    overflow: hidden;
    background-color: ${theme.palette.mode === "dark" ? grey[900] : "#fff"};
    border-radius: 8px;
    border: 1px solid ${theme.palette.mode === "dark" ? grey[700] : grey[200]};
    box-shadow: 0 4px 12px
      ${theme.palette.mode === "dark" ? "rgb(0 0 0 / 0.5)" : "rgb(0 0 0 / 0.2)"};
    padding: 24px;
    color: ${theme.palette.mode === "dark" ? grey[50] : grey[900]};

    & .modal-title {
      margin: 0;
      line-height: 1.5rem;
      margin-bottom: 8px;
    }

    & .modal-description {
      margin: 0;
      line-height: 1.5rem;
      font-weight: 400;
      color: ${theme.palette.mode === "dark" ? grey[400] : grey[800]};
      margin-bottom: 4px;
    }
  `
);
