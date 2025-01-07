using OpenTK;
using OpenTK.Graphics;
using OpenTK.Graphics.OpenGL;
using OpenTK.Input;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;

public class OpenTKWindow : GameWindow
{
    private List<Particle> particles;
    private Random random;
    private string text;

    public OpenTKWindow(int width, int height, string title)
        : base(width, height, GraphicsMode.Default, title)
    {
        particles = new List<Particle>();
        random = new Random();
    }

    protected override void OnLoad(EventArgs e)
    {
        base.OnLoad(e);
        GL.ClearColor(0.1f, 0.1f, 0.1f, 1.0f); // Background color
        InitializeParticles(600); // Initialize 1000 particles
    }

    protected override void OnRenderFrame(FrameEventArgs e)
    {
        base.OnRenderFrame(e);

        GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit);
        GL.LoadIdentity();

        foreach (var particle in particles)
        {
            particle.Render();
        }

        SwapBuffers();
    }

    protected override void OnUpdateFrame(FrameEventArgs e)
    {
        base.OnUpdateFrame(e);

        // Update each particle
        foreach (var particle in particles)
        {
            particle.Update((float)e.Time); // Update particle's position over time
        }
    }

    // Method to initialize particles randomly
    private void InitializeParticles(int count)
    {
        for (int i = 0; i < count; i++)
        {
            particles.Add(new Particle(
                position: new Vector3(
                    (float)(random.NextDouble() * 2 - 1),
                    (float)(random.NextDouble() * 2 - 1),
                    (float)(random.NextDouble() * 2 - 1)),
                velocity: new Vector3(
                    (float)(random.NextDouble() * 0.1 - 0.05),
                    (float)(random.NextDouble() * 0.1 - 0.05),
                    (float)(random.NextDouble() * 0.1 - 0.05)),
                size: (float)(random.NextDouble() * 0.1 + 0.05),
                color: new Vector4(
                    (float)random.NextDouble(),
                    (float)random.NextDouble(),
                    (float)random.NextDouble(),
                    1.0f)
            ));
        }
    }

    // Method to convert text to a series of points connected to form letters
    private void ArrangeParticlesIntoText(string text, int particleCount)
    {
        if (string.IsNullOrEmpty(text)) // Check if the text is null or empty
        {
            text = "Default Text"; // Assign default value if necessary
        }

        using (GraphicsPath path = new GraphicsPath())
        {
            // Create font and string format once
            Font font = new Font("Arial", 20, FontStyle.Bold);
            StringFormat stringFormat = StringFormat.GenericDefault;

            // Add string to path
            path.AddString(text, FontFamily.GenericSansSerif, (int)FontStyle.Bold, 20, new System.Drawing.PointF(10, 10), stringFormat);

            // Get points and initialize targetPositions with the correct capacity
            System.Drawing.PointF[] points = path.PathPoints;
            List<Vector3> targetPositions = new List<Vector3>(points.Length);

            // Normalize points and add to targetPositions
            foreach (var point in points)
            {
                targetPositions.Add(new Vector3(
                    (point.X - 100) / 100f, // Normalize X
                    (100 - point.Y) / 100f, // Normalize Y
                    0.0f // Fixed Z coordinate
                ));
            }

            // Connect points (this will make particles follow a path)
            int maxParticles = Math.Min(particleCount, targetPositions.Count);
            MessageBox.Show("Max particles: " + maxParticles);

            for (int i = 0; i < maxParticles; i++)
            {
                particles[i].SetTargetPosition(targetPositions[i]); // Set target position for particle
            }
        }
    }

    // Method to handle key press to change the text
    protected override void OnKeyDown(KeyboardKeyEventArgs e)
    {
        base.OnKeyDown(e);

        if (e.Key == Key.Space) // Press Space to arrange particles into a new pattern
        {
            ArrangeParticlesIntoText(this.text, particles.Count); // Update with new text
        }
    }
}
